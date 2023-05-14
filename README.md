# MTAtrack

This is the implementation of MTAtrack.    
This code is based on DETR: [[link]](https://github.com/facebookresearch/detr).

## Tracking demo
https://user-images.githubusercontent.com/114666579/212537480-d0932e1f-70c7-43e7-a4a5-1612ca539b52.mp4


## Dependencies
+ PyTorch 1.7.0
+ torchvision 0.8.1
+ cudatoolkit 10.2  
+ easydict
+ cython


## DataSets

```
${MTAtrack_ROOT}
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
python tracking/test.py MTAtrack_st --dataset trackingnet --threads 16
python lib/test/utils/transform_trackingnet.py --tracker_name MTAtrack_st
```

+ Lasot validation set
```
python tracking/test.py MTAtrack_st --dataset lasot --threads 16
python tracking/analysis_results.py  # need to modify tracker configs and names
```

+ GOT-10k validation set
```
python tracking/test.py MTAtrack_st --dataset got10k --threads 16
python lib/test/utils/transform_trackingnet.py --tracker_name MTAtrack_st
```

+ UAV123 validation set
```
python tracking/test.py MTAtrack_st baseline --dataset uav --threads 16
python tracking/analysis_results.py  # need to modify tracker configs and names
```

+ OTB100 validation set
```
python tracking/test.py MTAtrack_st baseline --dataset otb --threads 16
python tracking/analysis_results.py  # need to modify tracker configs and names
```

## Raw results
+ TrackingNet results  
[[trackingnet]](https://drive.google.com/file/d/1Hx9OtkxB6WGAWnjTTAkNkrNL0SO0z3Jf/view?usp=sharing)

+ Lasot results  
[[Lasot]](https://drive.google.com/file/d/1PAQXrI8mqufeEOwJ-uL87juchupvPHZB/view?usp=sharing)

+ GOT-10k results  
[[GOT-10k]](https://drive.google.com/file/d/1W5D8qVpi4DO6Q966ef-szsadVJtPOvnz/view?usp=sharing)

+ UAV123 results  
[[UAV123]](https://drive.google.com/file/d/1lb_tV1hWK92fA4QK-KnCvJYrYXnOG7DM/view?usp=share_link)

+ OTB100 results  
[[OTB100]](https://drive.google.com/file/d/1E3jhSkV8NMP6AQQ9CdgxF6McX2VpYNbQ/view?usp=sharing)
