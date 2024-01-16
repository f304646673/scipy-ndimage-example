import sys 
sys.path.append("..") 
from frame import *
import scipy.ndimage as ndimage

generate('lena.png', 'gaussian_filter1d.png', ndimage.gaussian_filter1d, 1, 10, 1)