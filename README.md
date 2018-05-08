# annotation_tools_misc
Python scripts to annotate and visualize.

Example usage for visAnnot.py:  
python visAnnot.py --dir ~/JPEGImages/savedata/

Example usage for collect.py:
python collect.py --image ~/JPEGImages/


Keyboard options for annotImg.py:  
"r" - reset drawing  
"b" - save bounding box  
"n" - save keypoint  
"s" - skip keypoint (if keypoint not visible, (-1,-1))  
"q" - save img name and go to next image

General pipeline:  
1.  ./script.sh  
2.  python collect.py --image ~/JPEGImages/
3.  python visAnnot.py --dir ~/JPEGImages/savedata/
4.  python split.py --dir ~/JPEGImages/savedata/
