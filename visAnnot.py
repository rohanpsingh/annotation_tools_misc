# import the necessary packages
import argparse
import csv
import cv2
import numpy as np


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True, help="Path to the image")
#ap.add_argument("-x", "--part_x", required=True, help="Image name (relative)")
#ap.add_argument("-y", "--part_y", required=True, help="Image name (relative)")
#ap.add_argument("-c", "--center", required=True, help="Image name (relative)")
#ap.add_argument("-s", "--scale", required=True, help="Image name (relative)")
ap.add_argument("-d", "--dir", required=True, help="directory for annotations")
args = vars(ap.parse_args())

imgl = open(args["dir"] + "img_names.txt", "r")
kpx = open(args["dir"] + "kpx.txt", "r")
kpy = open(args["dir"] + "kpy.txt", "r")
boxc = open(args["dir"] + "centers.txt", "r")
boxs = open(args["dir"] + "scale.txt", "r")


reader = csv.reader(imgl, delimiter="\t")
imgnames = list(reader)

reader = csv.reader(kpx, delimiter="\t")
kpxl = list(reader)

reader = csv.reader(kpy, delimiter="\t")
kpyl = list(reader)

reader = csv.reader(boxc, delimiter="\t")
centers = list(reader)

reader = csv.reader(boxs, delimiter="\t")
scales = list(reader)


def draw_bbox(image, center, scale):
        s = int(scale * 200)
        v0x = center[0] - s/2
        v0y = center[1] - s/2
        v1x = center[0] + s/2
        v1y = center[1] + s/2        
        cv2.rectangle(image, (v0x, v0y), (v1x,v1y), (0,255,0), 3)
        
        return image

def draw_kp(image, p):
        rad = 5
        cv2.circle(image, p, rad, (0,0,255), -1)

        return image


 
cv2.namedWindow("win", cv2.WINDOW_NORMAL)
cv2.resizeWindow("win", 1000,700)

assert len(imgnames) == len(kpxl) == len(kpyl) == len(centers) == len(scales) 

for i in range(0, len(imgnames)):

        image = cv2.imread( str(imgnames[i][0]))
        print str(imgnames[i][0])
        cpx = int(float(centers[i][0]))
        cpy = int(float(centers[i][1]))
        scale = float(scales[i][0])
        
        image = draw_bbox(image, (cpx,cpy), scale)

        for j in range(0, 6):
                kpx = int(float(kpxl[i][j]))
                kpy = int(float(kpyl[i][j]))
                image = draw_kp(image, (kpx, kpy))


        cv2.imshow("win", image)
        cv2.waitKey(0)


        
        
cv2.destroyAllWindows()
