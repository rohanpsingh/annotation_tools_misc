#!/usr/bin/env bash

echo "generating annotations"
#IMG_DIR="/home/rohan/rohan_m15x/dataset/yellow_tool/images1/frames"
IMG_DIR="/home/rohan/Desktop/oppo_cam/JPEGImages"
COUNT=0

mkdir -p $IMG_DIR/savedata/keypoints
mkdir -p $IMG_DIR/savedata/center
mkdir -p $IMG_DIR/savedata/scale

for img in $IMG_DIR/IMG*; do 

    printf "\n\n$img\n"
    printf -v num '%05d' $COUNT
    python annotImg.py --image $img --file $num --data $IMG_DIR || break
    ((COUNT++))

done
