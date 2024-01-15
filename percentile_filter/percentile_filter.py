import numpy as np
from PIL import Image
import scipy.ndimage as ndimage

source = np.array(Image.open('lena.png'))

colorDim3List = np.dsplit(source, 3)
red = colorDim3List[0].reshape(source.shape[0], source.shape[1])
green = colorDim3List[1].reshape(source.shape[0], source.shape[1])
blue = colorDim3List[2].reshape(source.shape[0], source.shape[1])

def percentile_filter(red, green, blue, percentile, size):
    redPercentileFilter =  ndimage.percentile_filter(red, percentile=percentile, size=size)
    greenPercentileFilter = ndimage.percentile_filter(green, percentile=percentile, size=size)
    bluePercentileFilter =  ndimage.percentile_filter(blue, percentile=percentile, size=size)
    return np.dstack((redPercentileFilter, greenPercentileFilter, bluePercentileFilter))

varrays = []
harrays = []
for i in range(1, 10):
    percentile_filter3D = percentile_filter(red, green, blue, i, i)
    harrays.append(percentile_filter3D)
    if i % 3 == 0:
        varrays.append(np.hstack(harrays))
        harrays = []
        
full3D = np.vstack(varrays)
Image.fromarray(full3D).save('percentile_filter.png')