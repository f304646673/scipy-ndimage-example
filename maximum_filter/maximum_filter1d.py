import sys 
sys.path.append("..") 
from frame import *
import scipy.ndimage as ndimage

generate('lena.png', 'maximum_filter1d.png', ndimage.maximum_filter1d, 1, 10, 1)