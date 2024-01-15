import numpy as np
from PIL import Image
import scipy.ndimage as ndimage

source = np.array(Image.open('lena.png'))

colorDim3List = np.dsplit(source, 3)
red = colorDim3List[0].reshape(source.shape[0], source.shape[1])
green = colorDim3List[1].reshape(source.shape[0], source.shape[1])
blue = colorDim3List[2].reshape(source.shape[0], source.shape[1])

def prewitt(red, green, blue):
    redPrewitt =  ndimage.prewitt(red)
    greenPrewitt = ndimage.prewitt(green)
    bluePrewitt =  ndimage.prewitt(blue)
    return np.dstack((redPrewitt, greenPrewitt, bluePrewitt))

prewitt3D = prewitt(red, green, blue)
Image.fromarray(prewitt3D).save('prewitt.png')