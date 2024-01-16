import numpy as np
from PIL import Image
import scipy.ndimage as ndimage

source = np.array(Image.open('lena.png'))

modeList = ['reflect', 'grid-mirror', 'constant', 'grid-constant', 'nearest', 'mirror', 'grid-wrap', 'wrap']
for mode in modeList:
    target = ndimage.shift(source, (30, 100, 0), mode=mode)
    Image.fromarray(target).save('shift_' + mode + '.png')