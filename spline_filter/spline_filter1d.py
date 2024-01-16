import sys 
sys.path.append("..") 
from frame import *
import scipy.ndimage as ndimage

def func(*args):
    return ndimage.spline_filter1d(args[0], args[1]).astype(np.uint8)

generate('lena.png', 'spline_filter1d.png', func, 2, 5, 1)