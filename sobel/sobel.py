import numpy as np
from PIL import Image
import scipy.ndimage as ndimage

source = np.array(Image.open('lena.png'))

colorDim3List = np.dsplit(source, 3)
red = colorDim3List[0].reshape(source.shape[0], source.shape[1])
green = colorDim3List[1].reshape(source.shape[0], source.shape[1])
blue = colorDim3List[2].reshape(source.shape[0], source.shape[1])

def sobel(red, green, blue):
    redSobel =  ndimage.sobel(red)
    greenSobel = ndimage.sobel(green)
    blueSobel =  ndimage.sobel(blue)
    return np.dstack((redSobel, greenSobel, blueSobel))

sobel3D = sobel(red, green, blue)
Image.fromarray(sobel3D).save('sobel.png')