import numpy as np
from PIL import Image
import scipy.ndimage as ndimage

source = np.array(Image.open('lena.png'))
colorDim3List = np.dsplit(source, 3)
red = colorDim3List[0].reshape(source.shape[0], source.shape[1])
green = colorDim3List[1].reshape(source.shape[0], source.shape[1])
blue = colorDim3List[2].reshape(source.shape[0], source.shape[1])

def correlate(red, green, blue, rows_columns):
    weights = np.eye(rows_columns)
    redCorrelate =  ndimage.correlate(red, weights)
    greenCorrelate = ndimage.correlate(green, weights)
    blueCorrelate =  ndimage.correlate(blue, weights)
    return np.dstack((redCorrelate, greenCorrelate, blueCorrelate))


varrays = []
harrays = []
for i in range(1, 10):
    correlate3D = correlate(red, green, blue, i)
    harrays.append(correlate3D)
    if i % 3 == 0:
        varrays.append(np.hstack(harrays))
        harrays = []    
    
full3D = np.vstack(varrays)
Image.fromarray(full3D).save('correlate.png')