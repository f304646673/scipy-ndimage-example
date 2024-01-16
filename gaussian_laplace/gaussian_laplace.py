import sys 
sys.path.append("..") 
from frame import *
import scipy.ndimage as ndimage

generate('lena.png', 'gaussian_laplace.png', ndimage.gaussian_laplace, 0.2, 1.9, 0.2)