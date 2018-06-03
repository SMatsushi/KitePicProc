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

win_name = "Trackbar"
# OpenCVのTrackbar便利クラス
class CVTrackbar:
    def __init__(self, param_name, win_name, param_min, param_max, update_func=doNothing):
        self._update_func = update_func
        self._trackbar = cv2.createTrackbar(param_name, win_name, param_min, param_max, self._callback)
        self._param_name = param_name
        self._win_name = win_name

    # Trackbarの値を参照
    def value(self):
        return cv2.getTrackbarPos(self._param_name, self._win_name)

    # Trackbarの値を設定
    def setValue(self, value):
        cv2.setTrackbarPos(self._param_name, self._win_name, value)

    def _callback(self, x):
        self._update_func(x)

    # TrackbarのCallbackを設定
    def setCallBack(self, update_func):
        self._update_func = update_func

low_threshold_trackbar = CVTrackbar("LowThr", win_name, 0, 200)
low_threshold_trackbar.setValue(100)
high_threshold_trackbar = CVTrackbar("HiThr", win_name, 0, 200)
high_threshold_trackbar.setValue(100)

# reading original jpeg image
org_img  = cv2.imread(infile, cv2.IMREAD_UNCHANGED)

# reading it in gray scale
gray_img  = cv2.imread(infile, cv2.IMREAD_GRAYSCALE)

# detect edge
# edges_img = cv2.Canny(gray_img, 50, 110)
edges_img = cv2.Canny(gray_img, low_threshold_trackbar.value(), upper_threshold_trackbar.value())

# plt.subplot(121),plt.imshow(org_img,cmap = 'Accent')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(121),plt.imshow(gray_img,cmap = 'gray')
plt.title('Gray Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges_img,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
# terminating
# cv2.waitKey(0)
# cv2.destroyAllWindows()

