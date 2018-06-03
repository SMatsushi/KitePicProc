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
from PIL import Image
import numpy as np
from docopt import docopt

# args = sys.argv
# print(args)
# print('arg[1] = '+args[1])
args = docopt(__doc__)

infile = args['<jpeg_in>']
# reading original jpeg image
img  = Image.open(infile)

# get width and height of original image
width, height = img.size

# create Image object in the same size of original
img2 = Image.new('RGB', (width, height))

img_pixels = []
for y in range(height):
    for x in range(width):
        # (x, y) = (0, 0) is left upper corner
        # get pixel at (x, y) and append it to img_pixels
        img_pixels.append(img.getpixel((x, y)))
# convert img_pixels to nmmpy array for ease of caliculation later
img_pixels = np.array(img_pixels)

img.show()
