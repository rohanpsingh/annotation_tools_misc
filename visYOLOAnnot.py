# usage $ python click_and_crop.py --image sample.jpg
# import the necessary packages
import argparse
import csv
import cv2
import os
import numpy as np


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image directory")
ap.add_argument("-b", "--bbox", required=True, help="Path to label directory")
ap.add_argument("-c", "--class", required=True, help="Select class to visualize")
ap.add_argument("-s", "--sec", required=True, help="Delay for visualization")
args = vars(ap.parse_args())


def draw_bbox(image, center, w, h):
        v0x = center[0] - w/2
        v0y = center[1] - h/2
        v1x = center[0] + w/2
        v1y = center[1] + h/2        
        cv2.rectangle(image, (v0x, v0y), (v1x,v1y), (0,255,0), 3)
        return image

 
cv2.namedWindow("win", cv2.WINDOW_NORMAL)
cv2.resizeWindow("win", 1000,700)

for img in os.listdir(args["image"]):
        if img.endswith("jpg"):
                print(os.path.splitext(img)[0])
                image = cv2.imread(os.path.join(args["image"], img))
                imgh = int(np.size(image,0))
                imgw = int(np.size(image,1))
                bbox = open(os.path.join(args["bbox"], os.path.splitext(img)[0]) + ".txt", "r")
                reader = csv.reader(bbox, delimiter="\t")
                label = list(reader)
                for i in range(0,len(label)):
                        if int(label[i][0])==int(args["class"]):
                                cpx = int(float(label[i][1]) * imgw)
                                cpy = int(float(label[i][2]) * imgh)
                                w =  int(float(label[i][3]) * imgw)
                                h =  int(float(label[i][4]) * imgh)
                                image = draw_bbox(image, (cpx,cpy), w, h)
                cv2.imshow("win", image)
                cv2.waitKey(int(args["sec"]))
        
        
cv2.destroyAllWindows()
