# Introduction
## Dependency
## Dataset Preparation & Preprocessing
- Download KITTI data and our pretrained model
	- This shell ```KITTI/downloader.sh``` can be used to download the KITTI images and pretrained model
		- the shell will only keep the left camera color images (image_03 folder) and delete other data
		- the downloaded images will be placed at ```KITTI/images/00/```, ```KITTI/images/01```, ...
		- the images offered by KITTI is already rectified
		- the direct [download link](https://drive.google.com/file/d/1l0s3rYWgN8bL0Fyofee8IhN-0knxJF22/view) of pretrained model
	- Download the ground truth pose from [KITTI Visual Odometry](http://www.cvlibs.net/datasets/kitti/eval_odometry.php)
		- you need to enter your email to request the pose data [here](http://www.cvlibs.net/download.php?file=data_odometry_poses.zip)
		- and place the ground truth pose at ```KITTI/pose_GT/```


