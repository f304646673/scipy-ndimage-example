import sys 
sys.path.append("..") 
from frame import *
import scipy.ndimage as ndimage

def func(*args):
    return ndimage.uniform_filter1d(args[0], args[1])

generate('lena.png', 'uniform_filter1d.png', func, 1, 10, 1)