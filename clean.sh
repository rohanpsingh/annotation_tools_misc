#!/usr/bin/env bash

IMG_DIR="/home/rohan/Desktop/oppo_cam/JPEGImages"

read -p "Are you sure you want to continue? <y/N> " prompt
if [[ $prompt == "y" || $prompt == "Y" || $prompt == "yes" || $prompt == "Yes" ]]
then
    mkdir $IMG_DIR/trash_annot
    cp -r $IMG_DIR/savedata $IMG_DIR/trash_annot
    gvfs-trash $IMG_DIR/trash_annot
    rm -rf $IMG_DIR/savedata
    rm -rf *~
else
  exit 0
fi

