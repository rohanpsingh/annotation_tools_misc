import argparse
import csv
import numpy as np
import random

train_len = 8

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dir", required=True, help="directory for annotations")
args = vars(ap.parse_args())

imgl = open(args["dir"] + "img_names.txt", "r")
kpx = open(args["dir"] + "kpx.txt", "r")
kpy = open(args["dir"] + "kpy.txt", "r")
boxc = open(args["dir"] + "centers.txt", "r")
boxs = open(args["dir"] + "scale.txt", "r")

img_lines = imgl.readlines()
kpx_lines = kpx.readlines()
kpy_lines = kpy.readlines()
cen_lines = boxc.readlines()
sca_lines = boxs.readlines()

imgl_train = open(args["dir"] + "img_names_train.txt", "w")
kpx_train = open(args["dir"] + "kpx_train.txt", "w")
kpy_train = open(args["dir"] + "kpy_train.txt", "w")
boxc_train = open(args["dir"] + "centers_train.txt", "w")
boxs_train = open(args["dir"] + "scale_train.txt", "w")

imgl_valid = open(args["dir"] + "img_names_valid.txt", "w")
kpx_valid = open(args["dir"] + "kpx_valid.txt", "w")
kpy_valid = open(args["dir"] + "kpy_valid.txt", "w")
boxc_valid = open(args["dir"] + "centers_valid.txt", "w")
boxs_valid = open(args["dir"] + "scale_valid.txt", "w")

valid_inds = range(len(img_lines))
train_inds = []
for i in range(0, train_len):
    t = random.choice(valid_inds)
    train_inds.append(t)
    valid_inds.remove(t)


for i in train_inds:
    imgl_train.write(img_lines[i])
    kpx_train.write(kpx_lines[i])
    kpy_train.write(kpy_lines[i])    
    boxc_train.write(cen_lines[i])
    boxs_train.write(sca_lines[i])

for i in valid_inds:
    imgl_valid.write(img_lines[i])
    kpx_valid.write(kpx_lines[i])
    kpy_valid.write(kpy_lines[i])    
    boxc_valid.write(cen_lines[i])
    boxs_valid.write(sca_lines[i])

imgl_train.close()
kpx_train.close()
kpy_train.close()
boxc_train.close()
boxs_train.close()

imgl_valid.close()
kpx_valid.close()
kpy_valid.close()
boxc_valid.close()
boxs_valid.close()

