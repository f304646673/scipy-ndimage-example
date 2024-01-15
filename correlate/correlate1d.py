import numpy as np
from PIL import Image
import scipy.ndimage as ndimage

source = np.array(Image.open('lena.png'))

varrays = []
harrays = []
for i in range(1, 10):
    weights = np.ones(i)
    convolve3D = ndimage.correlate1d(source, weights, axis=-1)
    harrays.append(convolve3D)
    if i % 3 == 0:
        varrays.append(np.hstack(harrays))
        harrays = [] 
    
Image.fromarray(np.vstack(varrays)).save('correlate1d.png')