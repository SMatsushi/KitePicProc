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
from matplotlib import pyplot as plt
from docopt import docopt

args = docopt(__doc__)

infile = args['<jpeg_in>']

def doNothing(self):
    pass

cv2.namedWindow('edge')
cv2.namedWindow('orig')
cv2.createTrackbar('LowThs', 'edge', 0, 200, doNothing)
cv2.createTrackbar('HighThs', 'edge', 0, 300, doNothing)

# reading original jpeg image
org_img  = cv2.imread(infile, cv2.IMREAD_UNCHANGED)
cv2.imshow('image', org_img)

# reading it in gray scale
gray_img  = cv2.imread(infile, cv2.IMREAD_GRAYSCALE)

# plt.subplot(121),plt.imshow(org_img,cmap = 'Accent')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# display gray image to edit by plt
plt.subplot(121),plt.imshow(gray_img,cmap = 'gray')
plt.title('Gray Image'), plt.xticks([]), plt.yticks([])
plt.show()

low = 100
high = 200
while (1):
    # detect edge
    # edges_img = cv2.Canny(gray_img, 50, 110)
    edges_img = cv2.Canny(gray_img, low, high)

    cv2.imshow('edge', edges_img)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get threashold value
    low = cv2.getTrackbarPos('LowThs', 'image')
    high = cv2.getTrackbarPos('HighThs', 'image')

#    plt.redraw()


# terminating
# cv2.waitKey(0)
# cv2.destroyAllWindows()

