#!/usr/bin/env bash

COUNT=0

case $1 in
    --imgdir=*)
    IMG_DIR="${1#*=}"
    case $2 in
	--clean)
	echo "cleaning.."
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
	;;
	--start)
	echo "generating annotations.."
	mkdir -p $IMG_DIR/savedata/keypoints
	mkdir -p $IMG_DIR/savedata/center
	mkdir -p $IMG_DIR/savedata/scale
	mkdir -p $IMG_DIR/savedata/yolo_annot
	for img in $IMG_DIR/frame_*; do 
	    printf "\n\n$img\n"
	    imgname=${img#$IMG_DIR/}
	    imgname=${imgname%.jpg}
	    printf -v num '%05d' $COUNT
	    python annotImg.py --image $imgname --file $num --data $IMG_DIR || break
	    ((COUNT++))
	done
	;;
	*)
	echo "argument error"
        # unknown option
	;;
    esac
    ;;
    *)
    echo "argument error"
    # unknown option
    ;;
esac


