import numpy as np
from PIL import Image
import scipy.ndimage as ndimage

source = np.array(Image.open('lena.png'))

colorDim3List = np.dsplit(source, 3)
red = colorDim3List[0].reshape(source.shape[0], source.shape[1])
green = colorDim3List[1].reshape(source.shape[0], source.shape[1])
blue = colorDim3List[2].reshape(source.shape[0], source.shape[1])

def uniform_filter(red, green, blue, size):
    redUniform =  ndimage.uniform_filter(red, size=size)
    greenUniform = ndimage.uniform_filter(green, size=size)
    blueUniform =  ndimage.uniform_filter(blue, size=size)
    return np.dstack((redUniform, greenUniform, blueUniform))

varrays = []
harrays = []
for i in range(1, 10):
    uniform_filter3D = uniform_filter(red, green, blue, i)
    harrays.append(uniform_filter3D)
    if i % 3 == 0:
        varrays.append(np.hstack(harrays))
        harrays = []
        
full3D = np.vstack(varrays)
Image.fromarray(full3D).save('uniform_filter.png')
