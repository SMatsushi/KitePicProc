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

# reading original jpeg image
## org_img  = cv2.imread(infile, cv2.IMREAD_UNCHANGED)
## cv2.imshow('image', org_img)

# reading it in gray scale
gray_img  = cv2.imread(infile, cv2.IMREAD_GRAYSCALE)

# plt.subplot(121),plt.imshow(org_img,cmap = 'Accent')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# display gray image to edit by plt
plt.subplot(121),plt.imshow(gray_img,cmap = 'gray')
plt.title('Gray Image'), plt.xticks([]), plt.yticks([])

# detect edge
low = 100
high = 200
edge_img = cv2.Canny(gray_img, low, high)
plt.subplot(122),plt.imshow(edge_img,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

# show
plt.show()

# terminating
cv2.waitKey(0)
cv2.destroyAllWindows()

