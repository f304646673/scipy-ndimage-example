import sys 
sys.path.append("..") 
from frame import *
import scipy.ndimage as ndimage

def func(*args):
    return ndimage.prewitt(args[0])

generate('lena.png', 'prewitt.png', func, 1, 2, 1)