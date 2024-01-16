import sys 
sys.path.append("..") 
from frame import *
import scipy.ndimage as ndimage

generate('lena.png', 'median_filter.png', ndimage.median_filter, 1, 10, 1)