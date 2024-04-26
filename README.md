# Introduction
## Dependency
- We tested our project at Ubuntu 20.04 and Ubuntu 22.04LTS
- You can check the configuration file at `deepVO.yml` and you can use `requirements.txt` file to generate conda env
## Real-world KITTI Dataset Preparation & Preprocessing
- Download KITTI real-world dataset at [here](https://www.cvlibs.net/datasets/kitti/)
   - This project used the monocular data from KITTI: please click `Odometry -> the Download odometry data set (color, 65 GB)`, which includes 10 sequences with provided ground truth for training
- Make sure you have downloaded the pose ground truth of the corresponding KITTI dataset sequences



- ## CARLA Synthetic Dataset Generation
- ### Preparation
- Download [CARLA v0.9.10](https://carla-releases.s3.eu-west-3.amazonaws.com/Linux/CARLA_0.9.10.tar.gz) and unzip it under `./carla`. Follow the install instruction of `scenario_runner` of commit [ad71a2c](https://github.com/carla-simulator/scenario_runner/tree/ad71a2c7ed012d735be2b1158fca51b0761ff26b).
- ### Data Collection
- Turn on CARLA as default and then run the following shell script.
- `cd ./carla-nuscenes/scripts`
- `bash routes_baselines.sh`
- LiDAR configurations can be accessed at `./carla-nuscenes/hyperparams`. Camera configurations can be accessed in `./carla-nuscenes/scenario_runner/lidar.py`. The density of Vehicles and Pedestrians can be accessed on `Line 397-422` in `./carla-nuscenes/scenario_runner/srunner/scenarios/route_scenario.py`. The datasets can be accessed at `./carla-nuscenes/dataset`.
- Run the following code to create NuScenes-formatted labels.
- `cp -r ./carla-nuscenes/dataset/[YOUR LIDAR PLACEMENT]/training/label_2 ./NuScenes_generate/label_2`
- `python ./NuScenes_generate/create_test_wide.py`
- `python ./NuScenes_generate/create_trainval_wide.py`
- Copy the folder `./NuScenes_generate/maps`, `./NuScenes_generate/v1.0-trainval` and `./NuScenes_generate/v1.0-test` to your dataset root. Replace the file `splits.py` in the NuScenes-devkit on your environment with our `./NuScenes_generate/splits.py`, otherwise the NuScenes-devkit can not recognize our dataset.

- Then, if you can see the following figures, your dataset is successfully generated 

<p align="center">
  <img src="CARLA_run.png" align="center" width="70%">

</p>
- ### Format Converter
- This part aims to convert the synthetic dataset to KITTI format, which is based on [work](https://website-name.com/)



      


