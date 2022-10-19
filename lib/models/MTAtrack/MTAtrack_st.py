"""
MTAtrack-ST Model (Spatio-Temporal).
"""
from .backbone import build_backbone
from .transformer import build_transformer
from .head import build_box_head, MLP
from lib.models.MTAtrack.MTAtrack_s import MTAtrackS


class MTAtrackST(MTAtrackS):
    """ This is the base class for Transformer Tracking """
    def __init__(self, backbone, transformer, box_head, num_queries,
                 aux_loss=False, head_type="CORNER", cls_head=None):
        """ Initializes the model.
        Parameters:
            backbone: torch module of the backbone to be used. See backbone.py
            transformer: torch module of the transformer architecture. See transformer.py
            num_queries: number of object queries.
            aux_loss: True if auxiliary decoding losses (loss at each decoder layer) are to be used.
        """
        super().__init__(backbone, transformer, box_head, num_queries,
                         aux_loss=aux_loss, head_type=head_type)
        self.cls_head = cls_head   #！！！

    def forward(self, img=None, seq_dict=None, mode="backbone", run_box_head=False, run_cls_head=False):
        if mode == "backbone":
            return self.forward_backbone(img)
        elif mode == "transformer":
            return self.forward_transformer(seq_dict, run_box_head=run_box_head, run_cls_head=run_cls_head)
        else:
            raise ValueError

    def forward_transformer(self, seq_dict, run_box_head=False, run_cls_head=False):
        if self.aux_loss:
            raise ValueError("Deep supervision is not supported.")
        # Forward the transformer encoder and decoder
        output_embed, enc_mem0, enc_mem5 = self.transformer(seq_dict["feat"], seq_dict["mask"], self.query_embed.weight,
                                                 seq_dict["pos"], return_encoder_output=True)
        # Forward the corner head
        out, outputs_coord = self.forward_head(output_embed, enc_mem0, enc_mem5, run_box_head=run_box_head, run_cls_head=run_cls_head)  #改变了！！
        return out, outputs_coord, output_embed

    def forward_head(self, hs, memory0, memory5, run_box_head=False, run_cls_head=False):
        """
        hs: output embeddings (1, B, N, C)
        memory: encoder embeddings (HW1+HW2, B, C)"""
        out_dict = {}
        if run_cls_head:
            # forward the classification head
            out_dict.update({'pred_logits': self.cls_head(hs)[-1]})  #classification
        if run_box_head:
            # forward the box prediction head
            out_dict_box, outputs_coord = self.forward_box_head(hs, memory0, memory5)
            # merge results
            out_dict.update(out_dict_box)
            return out_dict, outputs_coord
        else:
            return out_dict, None


def build_MTAtrackst(cfg):
    backbone = build_backbone(cfg)  # backbone and positional encoding are built together
    transformer = build_transformer(cfg)
    box_head = build_box_head(cfg)
    cls_head = MLP(cfg.MODEL.HIDDEN_DIM, cfg.MODEL.HIDDEN_DIM, 1, cfg.MODEL.NLAYER_HEAD)   #加了一个多层感知器来预测检测的准确率？？
    model = MTAtrackST(
        backbone,
        transformer,
        box_head,
        num_queries=cfg.MODEL.NUM_OBJECT_QUERIES,
        aux_loss=cfg.TRAIN.DEEP_SUPERVISION,
        head_type=cfg.MODEL.HEAD_TYPE,
        cls_head=cls_head
    )

    return model
