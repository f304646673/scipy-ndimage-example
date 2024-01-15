import numpy as np
from PIL import Image
import scipy.ndimage as ndimage

source = np.array(Image.open('lena.png'))

colorDim3List = np.dsplit(source, 3)
red = colorDim3List[0].reshape(source.shape[0], source.shape[1])
green = colorDim3List[1].reshape(source.shape[0], source.shape[1])
blue = colorDim3List[2].reshape(source.shape[0], source.shape[1])

def maximum_filter(red, green, blue, size):
    redMaximumFilter =  ndimage.maximum_filter(red, size=size)
    greenMaximumFilter = ndimage.maximum_filter(green, size=size)
    blueMaximumFilter =  ndimage.maximum_filter(blue, size=size)
    return np.dstack((redMaximumFilter, greenMaximumFilter, blueMaximumFilter))

varrays = []
harrays = []
for i in range(1, 10):
    maximum_filter3D = maximum_filter(red, green, blue, i)
    harrays.append(maximum_filter3D)
    if i % 3 == 0:
        varrays.append(np.hstack(harrays))
        harrays = []
        
full3D = np.vstack(varrays)
Image.fromarray(full3D).save('maximum_filter.png')