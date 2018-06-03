#!/usr/bin/env python

__doc__ = """{f}

Usage:
    {f} <jpeg_in> [-v | --verbose]
    {f} -f | --help

Options:
    -o --output <jpeg_out>   Output jpeg filename
    -v --verbose             Show verbose message
    -h --help                Show this help and exit
""".format(f=__file__)

import sys
import cv2
import numpy as np
from docopt import docopt

args = docopt(__doc__)

infile = args['<jpeg_in>']
# reading original jpeg image
org_img  = cv2.imread(infile, cv2.IMREAD_UNCHANGED)

# reading it in gray scale
gray_img  = cv2.imread(infile, cv2.IMREAD_GRAYSCALE)

# detect edge
canny_img = cv2.Canny(gray_img, 50, 110)

ORG_WIN = "org"
GRY_WIN = "gray"
CAN_WIN = "canny"

cv2.imshow(ORG_WIN, org_img)
cv2.imshow(GRY_WIN, gray_img)
cv2.imshow(CAN_WIN, canny_img)

# terminating
cv2.waitKey(0)
cv2.destroyAllWindows()

