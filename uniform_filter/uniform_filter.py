import sys 
sys.path.append("..") 
from frame import *
import scipy.ndimage as ndimage

def func(*args):
    return ndimage.uniform_filter(args[0], args[1])

generate('lena.png', 'uniform_filter.png', func, 1, 10, 1)