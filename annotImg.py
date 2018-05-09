# usage $ python click_and_crop.py --image sample.jpg
# import the necessary packages
import argparse
import cv2
import numpy as np
 
# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
x_start, y_start, x_end, y_end = 0, 0, 0, 0
cropping = False
getROI = False
refPt = []

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
ap.add_argument("-f", "--file", required=True, help="Image name (relative)")
ap.add_argument("-d", "--data", required=True, help="Path to savedata")
args = vars(ap.parse_args())
 
# load the image, clone it, and setup the mouse callback function
image = cv2.imread(args["data"] + "/" + args["image"] + ".jpg")
clone = image.copy()

imgw = 1./np.size(image,1)
imgh = 1./np.size(image,0)
print("imgsize:\t" + repr(1./imgw) + ", " + repr(1./imgh))

def click_and_crop(event, x, y, flags, param):
	# grab references to the global variables
	global x_start, y_start, x_end, y_end, cropping, getROI

	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONDOWN:
		x_start, y_start, x_end, y_end = x, y, x, y
		cropping = True

	elif event == cv2.EVENT_MOUSEMOVE:
		if cropping == True:
			x_end, y_end = x, y

	# check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		x_end, y_end = x, y
		cropping = False
		getROI = True

kp_file = open(args["data"] + "/savedata/keypoints/keypoints_" + args["file"] + ".csv", "w")
center_file = open(args["data"] + "/savedata/center/center_" + args["file"] + ".csv", "w")
scale_file = open(args["data"] + "/savedata/scale/scale_" + args["file"] + ".txt", "w")
yolo_file = open(args["data"] + "/savedata/yolo_annot/" + args["image"] + ".txt", "w")

def key_point(keyPt):
	kp_file.write(repr(keyPt[0]) + "," + repr(keyPt[1]) + "\n")
	print("keypt: " + repr(keyPt))

def bbox_center(center):
	center_file.write(repr(center[0]) + "," + repr(center[1]) + "\n")
	print("center: " + repr(center))

def bbox_scale(scale):
        scale_file.write(repr(scale) + "\n")
        print("scale: " + repr(scale))

def yolo_bbox(center, w, h):
        yolo_file.write("0\t" + repr(center[0]) + "\t" + repr(center[1]) + "\t" + repr(w) + "\t" + repr(h) + "\n")
        print("center: " + repr(center) + "\tw: " + repr(w) + "\th:" + repr(h))

 
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("image", 3000,2000)
cv2.setMouseCallback("image", click_and_crop)
 
# keep looping until the 'q' key is pressed
while True:

	i = image.copy()

	if not cropping and not getROI:
		cv2.imshow("image", image)

	elif cropping and not getROI:
		cv2.rectangle(i, (x_start, y_start), (x_end, y_end), (0, 255, 0), 2)
		cv2.imshow("image", i)

	elif not cropping and getROI:
		cv2.rectangle(image, (x_start, y_start), (x_end, y_end), (0, 255, 0), 2)
		cv2.imshow("image", image)

	key = cv2.waitKey(1) & 0xFF


	# if the 'r' key is pressed
	if key == ord("r"):
		image = clone.copy()
		getROI = False
 
	# if the 'n' key is pressed
	if key == ord("n"):
		image = clone.copy()
		keyPt = ((x_end + x_start)/2),((y_end + y_start)/2)
		key_point(keyPt)
		getROI = False

	# if the 's' key is pressed
	if key == ord("s"):
		image = clone.copy()
		keyPt = -1,-1
		key_point(keyPt)
		getROI = False
	

	# if the 'b' key is pressed
	if key == ord("b"):
		image = clone.copy()
                wd = abs(x_end - x_start)
                ht = abs(y_end - y_start)
                print(wd)
                print(ht)
		center =  ((x_end + x_start)/2),((y_end + y_start)/2)
		bbox_center(center)
                scale = max(wd,ht)/200.0
                bbox_scale(scale)
                wd *= imgw
                ht *= imgh
                center =  (imgw*(x_end + x_start)/2),(imgh*(y_end + y_start)/2)
                yolo_bbox(center, wd, ht)
		getROI = False

	 
	# if the 'q' key is pressed, break from the loop
	elif key == ord("q"):
                imgfile = open(args["data"] + "/savedata/img_names.txt", "a")
                imgfile.write(args["data"] + "/" + args["image"] + ".jpg" + "\n")
                imgfile.close()
		kp_file.close()
		center_file.close()
                yolo_file.close()
		break

cv2.destroyAllWindows()
