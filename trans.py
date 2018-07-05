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
from matplotlib.widgets import Slider, Button, RadioButtons
from docopt import docopt

args = docopt(__doc__)

infile = args['<jpeg_in>']

def doNothing(self):
    pass

plt.ion()
# plt.ioff()

#
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
#    l.set_ydata(amp*np.sin(2*np.pi*freq*t))
#    fig.canvas.draw_idle()

# reading original jpeg image
org_img  = cv2.imread(infile, cv2.IMREAD_UNCHANGED)
cv2.imshow('Original Image', org_img)
# plt.imshow(org_img) # does not work

# reading it in gray scale
gray_img  = cv2.imread(infile, cv2.IMREAD_GRAYSCALE)

# plt.subplot(121),plt.imshow(org_img,cmap = 'Accent')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# display gray image to edit by plt
plt.subplot(121),plt.imshow(gray_img,cmap = 'gray')
plt.title('Gray Image'), plt.xticks([]), plt.yticks([])

# detect edge
def draw_edge(low, high):
    edge_img = cv2.Canny(gray_img, low, high)
    plt.subplot(122),plt.imshow(edge_img,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

ini_low = 190
ini_high = 290
draw_edge(ini_low, ini_high)

# slider, button, radio buttons
axcolor = 'lightgoldenrodyellow'
# sliders
delta_f = 1
axlow = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axhigh = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

s_low  = Slider(axlow, 'Thres Low', 0, 200, valinit=ini_low, valstep=delta_f)
s_high = Slider(axhigh, 'Thres High', 0, 300, valinit=ini_high, valstep=delta_f)

def update(val):
    draw_edge(s_low.val, s_high.val)
    fig.canvas.draw_idle()

s_low.on_changed(update)
s_high.on_changed(update)

# button
## reset
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
reset_button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    s_low.reset()
    s_high.reset()
reset_button.on_clicked(reset)

## exit
exitax = plt.axes([0.65, 0.025, 0.1, 0.04])
exit_button = Button(exitax, 'Exit', color=axcolor, hovercolor='0.975')

def exit(event):
    cv2.destroyAllWindows()
    sys.exit()
exit_button.on_clicked(exit)

# radio button
rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)

def colorfunc(label):
    fig.canvas.draw_idle()
radio.on_clicked(colorfunc)

# show
## plt.draw()
plt.show()

# terminating
cv2.waitKey(0)
cv2.destroyAllWindows()

