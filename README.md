# MAtrack

This is the implementation of MAtrack.    
This code is based on DETR: [[link]](https://github.com/facebookresearch/detr).


## Dependencies
+ PyTorch 1.7.0
+ torchvision 0.8.1
+ cudatoolkit 10.2  
+ easydict
+ cython


## DataSets

```
${MAtrack_ROOT}
 -- data
     -- Lasot
         |-- airplane
         |-- basketball
         |-- bear
         ...
     -- GOT10k
         |-- test
         |-- train
         |-- val
     -- COCO
         |-- annotations
         |-- images
     -- TrackingNet
         |-- TRAIN_0
         |-- TRAIN_1
         ...
         |-- TRAIN_11
         |-- TEST
```

## Trained model
+ Download pre-trained weights into ```./checpoints```  
[[weights]](https://drive.google.com/file/d/1N0BgKRKuxJyGReBgcwmFuK77ka1k226Z/view?usp=sharing)

## Code

+ paths setting
```
python tracking/create_default_local_file.py --workspace_dir . --data_dir ./data --save_dir .
```

+ TrackingNet validation set
```
python tracking/test.py MAtrack_st --dataset trackingnet --threads 16
python lib/test/utils/transform_trackingnet.py --tracker_name MAtrack_st
```

+ Lasot validation set
```
python tracking/test.py MAtrack_st --dataset lasot --threads 16
python tracking/analysis_results.py
```

+ GOT-10k validation set
```
python tracking/test.py MAtrack_st --dataset got10k --threads 16
python lib/test/utils/transform_trackingnet.py --tracker_name MAtrack_st
```

## Raw results
+ TrackingNet results  
[[trackingnet]](https://drive.google.com/file/d/1Hx9OtkxB6WGAWnjTTAkNkrNL0SO0z3Jf/view?usp=sharing)

+ Lasot results  
[[Lasot]](https://drive.google.com/file/d/1PAQXrI8mqufeEOwJ-uL87juchupvPHZB/view?usp=sharing)

+ GOT-10k results  
[[GOT-10k]](https://drive.google.com/file/d/1W5D8qVpi4DO6Q966ef-szsadVJtPOvnz/view?usp=sharing)

