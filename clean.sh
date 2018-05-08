#!/usr/bin/env bash

read -p "Are you sure you want to continue? <y/N> " prompt
if [[ $prompt == "y" || $prompt == "Y" || $prompt == "yes" || $prompt == "Yes" ]]
then
    mkdir trash_annot
    cp -r savedata trash_annot
    gvfs-trash trash_annot
    rm -rf savedata/scale/*
    rm -rf savedata/center/*
    rm -rf savedata/keypoints/*
    rm -rf savedata/img_names.txt
    rm -rf *~
else
  exit 0
fi

