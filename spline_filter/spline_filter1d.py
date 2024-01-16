import numpy as np
from PIL import Image
import scipy.ndimage as ndimage

source = np.array(Image.open('lena.png'))

colorDim3List = np.dsplit(source, 3)
red = colorDim3List[0].reshape(source.shape[0], source.shape[1])
green = colorDim3List[1].reshape(source.shape[0], source.shape[1])
blue = colorDim3List[2].reshape(source.shape[0], source.shape[1])

def spline_filter1d(red, green, blue, order):
    redSplineFilter1d =  ndimage.spline_filter1d(red, order=order).astype(np.uint8)
    greenSplineFilter1d = ndimage.spline_filter1d(green, order=order).astype(np.uint8)
    blueSplineFilter1d =  ndimage.spline_filter1d(blue, order=order).astype(np.uint8)
    return np.dstack((redSplineFilter1d, greenSplineFilter1d, blueSplineFilter1d))

varrays = []
harrays = []
hindex = 0

for i in range(2, 6):
    spline_filter1d3D = spline_filter1d(red, green, blue, i)
    harrays.append(spline_filter1d3D)
    hindex += 1
    if hindex % 3 == 0:
        varrays.append(np.hstack(harrays))
        harrays = []
        hindex = 0
        
full3D = np.vstack(varrays)
Image.fromarray(full3D).save('spline_filter1d.png')