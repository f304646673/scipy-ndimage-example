import sys 
sys.path.append("..") 
from frame import *
import scipy.ndimage as ndimage

def func(*args):
    weights = np.eye(args[1])
    return ndimage.correlate(args[0], weights)

generate('lena.png', 'correlate.png', func, 1, 10, 1)