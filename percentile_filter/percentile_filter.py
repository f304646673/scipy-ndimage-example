import sys 
sys.path.append("..") 
from frame import *
import scipy.ndimage as ndimage

def func(*args):
    return ndimage.percentile_filter(args[0], percentile=args[1], size=args[1])

generate('lena.png', 'percentile_filter.png', func, 1, 10, 1)