import csv
import numpy
import glob
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image folder")
args = vars(ap.parse_args())

kpx = open(args["image"] + "/savedata/kpx.txt", "w")
kpy = open(args["image"] + "/savedata/kpy.txt", "w")
kpdir = args["image"] + "/savedata/keypoints/"
kpfilelist = sorted(glob.glob(kpdir + "*"))
for kpfile in kpfilelist:
        reader = csv.reader(open(kpfile, "r"), delimiter=",")
        x = list(reader)
        arr = numpy.array(x).astype("float").T
        numpy.savetxt(kpx, arr[0], fmt='%1.2f', newline='\t')
        numpy.savetxt(kpy, arr[1], fmt='%1.2f', newline='\t')
        kpx.write("\n")
        kpy.write("\n")

kpx.close()
kpy.close()


center = open(args["image"] + "/savedata/centers.txt", "w")
centerdir = args["image"] + "/savedata/center/"
cplist = sorted(glob.glob(centerdir + "*"))
for cpfile in cplist:
        reader = csv.reader(open(cpfile, "r"), delimiter=",")
        x = list(reader)
        arr = numpy.array(x).astype("float")
        numpy.savetxt(center, arr, fmt='%1.2f', delimiter="\t", newline='\n')

center.close()


scale = open(args["image"] + "/savedata/scale.txt", "w")
scaledir = args["image"] + "/savedata/scale/"
scalelist = sorted(glob.glob(scaledir + "*"))
for scalefile in scalelist:
        reader = csv.reader(open(scalefile, "r"), delimiter=",")
        x = list(reader)
        arr = numpy.array(x).astype("float")
        numpy.savetxt(scale, arr, fmt='%1.2f', delimiter="\t", newline='\n')

scale.close()
        



