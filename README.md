KitePicProc
# Description 
Converting a kite photograph in the sky to its flat artwork: Python (virtual env python3.5) + OpenCV (numpy, matplotlib) code

# Reference
## An introducion of Python Open CV
<https://codewords.recurse.com/issues/six/image-processing-101>  

## Instration guide
Install virtual env, python3.5 (not python2.7), openCV.
<https://github.com/piratefsh/image-processing-101>  

In python3.5 virtual env, install numpy, matplotlib with pip.
-----
### Maybe wrong procedure...
First I did followings, but they did not work:
> $ pip install docopt  

Problem happend. According to https://github.com/pypa/virtualenv/issues/788  
  But maybe it was not a fix.
> $ conda install -c anaconda virtualenv=15.1.0

### Correct procedure..
> $ git clone https://github.com/piratefsh/image-processing-101.git  
> $ cd image-processing-101/  
> $ pip install -r requirements.txt  
> $ conda create -n py3.5 python=3.5 anaconda  
> $ source /anaconda2/bin/activate py3.5  
> $ pip install opencv_python  

# Usage
## step1.
> $ source enable-py3_5.sh  
 or
> $ source /anaconda2/bin/activate py3.5  

## step2.
> $ trans.py daruma.jpg

Note) transPLI.py does not work yet.
