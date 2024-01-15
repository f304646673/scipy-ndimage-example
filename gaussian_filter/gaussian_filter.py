import numpy as np
from PIL import Image
import scipy.ndimage as ndimage

source = np.array(Image.open('lena.png'))

colorDim3List = np.dsplit(source, 3)
red = colorDim3List[0].reshape(source.shape[0], source.shape[1])
green = colorDim3List[1].reshape(source.shape[0], source.shape[1])
blue = colorDim3List[2].reshape(source.shape[0], source.shape[1])

def gaussian_filter(red, green, blue, sigma):
    redGaussian =  ndimage.gaussian_filter(red, sigma=sigma)
    greenGaussian = ndimage.gaussian_filter(green, sigma=sigma)
    blueGaussian =  ndimage.gaussian_filter(blue, sigma=sigma)
    return np.dstack((redGaussian, greenGaussian, blueGaussian))

varrays = []
harrays = []
for i in range(1, 10):
    gaussian3D = gaussian_filter(red, green, blue, i)
    harrays.append(gaussian3D)
    if i % 3 == 0:
        varrays.append(np.hstack(harrays))
        harrays = []         
        
full3D = np.vstack(varrays)
Image.fromarray(full3D).save('gaussian_filter.png')