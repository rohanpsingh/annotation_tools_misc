# annotation_tools_misc
Python scripts to annotate and visualize.

Example usage for visAnnot.py:
python visAnnot.py -i examples/imagenames.txt -x examples/kpx.txt -y examples/kpy.txt -c examples/center.txt -s examples/scale.txt

Example usage for collect.py:
python collect.py --image ~/JPEGImages/


Keyboard options for annotImg.py:
"r" - reset drawing
"b" - save bounding box
"n" - save keypoint
"s" - skip keypoint (if keypoint not visible, (-1,-1))
"q" - save img name and go to next image
