import numpy as np
from PIL import Image
import scipy.ndimage as ndimage

source = np.array(Image.open('lena.png'))

colorDim3List = np.dsplit(source, 3)
red = colorDim3List[0].reshape(source.shape[0], source.shape[1])
green = colorDim3List[1].reshape(source.shape[0], source.shape[1])
blue = colorDim3List[2].reshape(source.shape[0], source.shape[1])

def white_tophat(red, green, blue, size):
    redWhiteTophat =  ndimage.white_tophat(red, size=size)
    greenWhiteTophat = ndimage.white_tophat(green, size=size)
    blueWhiteTophat =  ndimage.white_tophat(blue, size=size)
    return np.dstack((redWhiteTophat, greenWhiteTophat, blueWhiteTophat))

varrays = []
harrays = []
hindex = 0
for i in range(1, 91, 10):
    white_tophat3D = white_tophat(red, green, blue, i)
    harrays.append(white_tophat3D)
    hindex += 1
    if hindex % 3 == 0:
        varrays.append(np.hstack(harrays))
        hindex = 0
        harrays = []
        
full3D = np.vstack(varrays)
Image.fromarray(full3D).save('white_tophat.png')