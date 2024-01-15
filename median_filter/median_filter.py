import numpy as np
from PIL import Image
import scipy.ndimage as ndimage

source = np.array(Image.open('lena.png'))

colorDim3List = np.dsplit(source, 3)
red = colorDim3List[0].reshape(source.shape[0], source.shape[1])
green = colorDim3List[1].reshape(source.shape[0], source.shape[1])
blue = colorDim3List[2].reshape(source.shape[0], source.shape[1])

def median_filter(red, green, blue, size):
    redMedianFilter =  ndimage.median_filter(red, size=size)
    greenMedianFilter = ndimage.median_filter(green, size=size)
    blueMedianFilter =  ndimage.median_filter(blue, size=size)
    return np.dstack((redMedianFilter, greenMedianFilter, blueMedianFilter))

varrays = []
harrays = []
for i in range(1, 10):
    median_filter3D = median_filter(red, green, blue, i)
    harrays.append(median_filter3D)
    if i % 3 == 0:
        varrays.append(np.hstack(harrays))
        harrays = []
        
full3D = np.vstack(varrays)
Image.fromarray(full3D).save('median_filter.png')