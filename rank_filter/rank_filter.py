import sys 
sys.path.append("..") 
from frame import *
import scipy.ndimage as ndimage

def func(*args):
    return ndimage.rank_filter(args[0], rank=args[1], size=args[1]*2)

generate('lena.png', 'rank_filter.png', func, 1, 10, 1)