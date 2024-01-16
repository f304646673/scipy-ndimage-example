import numpy as np
from PIL import Image
import scipy.ndimage as ndimage

source = np.array(Image.open('lena.png'))

colorDim3List = np.dsplit(source, 3)
red = colorDim3List[0].reshape(source.shape[0], source.shape[1])
green = colorDim3List[1].reshape(source.shape[0], source.shape[1])
blue = colorDim3List[2].reshape(source.shape[0], source.shape[1])

def black_tophat(red, green, blue, size):
    redBlackTophat =  ndimage.black_tophat(red, size=size)
    greenBlackTophat = ndimage.black_tophat(green, size=size)
    blueBlackTophat =  ndimage.black_tophat(blue, size=size)
    return np.dstack((redBlackTophat, greenBlackTophat, blueBlackTophat))

varrays = []
harrays = []
hindex = 0

for i in range(1, 91, 10):
    black_tophat3D = black_tophat(red, green, blue, i)
    harrays.append(black_tophat3D)
    hindex += 1
    if hindex % 3 == 0:
        varrays.append(np.hstack(harrays))
        harrays = []
        hindex = 0
        
full3D = np.vstack(varrays)
Image.fromarray(full3D).save('black_tophat.png')