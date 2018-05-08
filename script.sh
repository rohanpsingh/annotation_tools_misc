#!/usr/bin/env bash

echo "generating annotations"
#IMG_DIR="/home/rohan/rohan_m15x/dataset/yellow_tool/images1/frames"
IMG_DIR="/home/rohan/Desktop/oppo_cam/JPEGImages"
COUNT=0


for img in $IMG_DIR/frame*; do 

    printf "\n\n$img\n"
    printf -v num '%05d' $COUNT
    python annotImg.py --image $img --file $COUNT || break
    ((COUNT++))

done
