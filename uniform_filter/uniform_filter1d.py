import numpy as np
from PIL import Image
import scipy.ndimage as ndimage

source = np.array(Image.open('lena.png'))

colorDim3List = np.dsplit(source, 3)
red = colorDim3List[0].reshape(source.shape[0], source.shape[1])
green = colorDim3List[1].reshape(source.shape[0], source.shape[1])
blue = colorDim3List[2].reshape(source.shape[0], source.shape[1])

def uniform_filter1d(red, green, blue, size):
    redGaussian =  ndimage.uniform_filter1d(red, size=size)
    greenGaussian = ndimage.uniform_filter1d(green, size=size)
    blueGaussian =  ndimage.uniform_filter1d(blue, size=size)
    return np.dstack((redGaussian, greenGaussian, blueGaussian))

varrays = []
harrays = []
for i in range(1, 10):
    gaussian3D = uniform_filter1d(red, green, blue, i)
    harrays.append(gaussian3D)
    if i % 3 == 0:
        varrays.append(np.hstack(harrays))
        harrays = []
        
full3D = np.vstack(varrays)
Image.fromarray(full3D).save('uniform_filter1d.png')