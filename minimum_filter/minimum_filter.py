import sys 
sys.path.append("..") 
from frame import *
import scipy.ndimage as ndimage

generate('lena.png', 'minimum_filter.png', ndimage.minimum_filter, 1, 10, 1)