import sys 
sys.path.append("..") 
from frame import *
import scipy.ndimage as ndimage

def func(*args):
    return ndimage.white_tophat(args[0], args[1])

generate('lena.png', 'white_tophat.png', func, 1, 91, 10)