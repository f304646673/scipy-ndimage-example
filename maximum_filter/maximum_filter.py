import sys 
sys.path.append("..") 
from frame import *
import scipy.ndimage as ndimage

generate('lena.png', 'maximum_filter.png', ndimage.maximum_filter, 1, 10, 1)