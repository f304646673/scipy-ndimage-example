import sys 
sys.path.append("..") 
from frame import *
import scipy.ndimage as ndimage

generate('lena.png', 'black_tophat.png', ndimage.black_tophat, 1, 91, 10)