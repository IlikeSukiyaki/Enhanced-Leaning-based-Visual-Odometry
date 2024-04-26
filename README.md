# Introduction
## Dependency
- We tested our project at Ubuntu 20.04 and Ubuntu 22.04LTS
- You can check the configuration file at `deepVO.yml` and you can use `requirements.txt` file to generate conda env
## Dataset Preparation & Preprocessing
- Download KITTI real-world dataset at [here](https://www.cvlibs.net/datasets/kitti/)
   - This project used the monocular data from KITTI: please click `Odometry -> the Download odometry data set (color, 65 GB)`, which includes 10 sequences with provided ground truth for training
- Make sure you have downloaded the pose ground truth of the corresponding KITTI dataset sequences



- ## CARLA Dataset Generation
- ### Preparation
- Download [CARLA v0.9.10](https://carla-releases.s3.eu-west-3.amazonaws.com/Linux/CARLA_0.9.10.tar.gz) and unzip it under `./carla`. Follow the install instruction of `scenario_runner` of commit [ad71a2c](https://github.com/carla-simulator/scenario_runner/tree/ad71a2c7ed012d735be2b1158fca51b0761ff26b).

      


