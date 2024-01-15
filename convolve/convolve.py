import numpy as np
from PIL import Image
import scipy.ndimage as ndimage

source = np.array(Image.open('lena.png'))
colorDim3List = np.dsplit(source, 3)
red = colorDim3List[0].reshape(source.shape[0], source.shape[1])
green = colorDim3List[1].reshape(source.shape[0], source.shape[1])
blue = colorDim3List[2].reshape(source.shape[0], source.shape[1])

def convolve(red, green, blue, rows_columns):
    weights = np.eye(rows_columns)
    redConvolve =  ndimage.convolve(red, weights)
    greenConvolve = ndimage.convolve(green, weights)
    blueConvolve =  ndimage.convolve(blue, weights)
    return np.dstack((redConvolve, greenConvolve, blueConvolve))

varrays = []
harrays = []
for i in range(1, 10):
    convolve3D = convolve(red, green, blue, i)
    harrays.append(convolve3D)
    if i % 3 == 0:
        varrays.append(np.hstack(harrays))
        harrays = []    

full3D = np.vstack(varrays)
Image.fromarray(full3D).save('convolve.png')
    