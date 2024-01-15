import numpy as np
from PIL import Image
import scipy.ndimage as ndimage

source = np.array(Image.open('lena.png'))

colorDim3List = np.dsplit(source, 3)
red = colorDim3List[0].reshape(source.shape[0], source.shape[1])
green = colorDim3List[1].reshape(source.shape[0], source.shape[1])
blue = colorDim3List[2].reshape(source.shape[0], source.shape[1])

def minimum_filter(red, green, blue, size):
    redMinimumFilter =  ndimage.minimum_filter(red, size=size)
    greenMinimumFilter = ndimage.minimum_filter(green, size=size)
    blueMinimumFilter =  ndimage.minimum_filter(blue, size=size)
    return np.dstack((redMinimumFilter, greenMinimumFilter, blueMinimumFilter))

varrays = []
harrays = []
for i in range(1, 10):
    minimum_filter3D = minimum_filter(red, green, blue, i)
    harrays.append(minimum_filter3D)
    if i % 3 == 0:
        varrays.append(np.hstack(harrays))
        harrays = []
        
full3D = np.vstack(varrays)
Image.fromarray(full3D).save('minimum_filter.png')
