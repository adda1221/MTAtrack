import torch
import numpy as np
from lib.utils.misc import NestedTensor


class Preprocessor(object):
    def __init__(self):
        self.mean = torch.tensor([0.485, 0.456, 0.406]).view((1, 3, 1, 1)).cuda()  #view改变数组的形状
        self.std = torch.tensor([0.229, 0.224, 0.225]).view((1, 3, 1, 1)).cuda()

    def process(self, img_arr: np.ndarray, amask_arr: np.ndarray):
        # Deal with the image patch
        img_tensor = torch.tensor(img_arr).cuda().float().permute((2,0,1)).unsqueeze(dim=0)   #permute：对数组的元素进行换位   unsqueeze(dim=0) 增加一维
        img_tensor_norm = ((img_tensor / 255.0) - self.mean) / self.std  # (1,3,H,W)
        # Deal with the attention mask
        amask_tensor = torch.from_numpy(amask_arr).to(torch.bool).cuda().unsqueeze(dim=0)  # (1,H,W)   #torch.from_numpy()方法把数组转换成张量，且二者共享内存，对张量进行修改比如重新赋值，那么原始数组也会相应发生改变。
        return NestedTensor(img_tensor_norm, amask_tensor)
    #当mask的数据类型是torch.uint8或者torch.bool时，此时的tensor用作mask, tensor中的1对应的行/列保留，0对应的行/列舍去。且被mask的维度必须与原始tensor的维度一致，即mask.size(0)==t.shape(0）。




