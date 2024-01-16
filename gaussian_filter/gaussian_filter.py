import sys 
sys.path.append("..") 
from frame import *
import scipy.ndimage as ndimage

generate('lena.png', 'gaussian_filter.png', ndimage.gaussian_filter, 1, 10, 1)