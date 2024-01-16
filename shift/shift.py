import numpy as np
from PIL import Image
import scipy.ndimage as ndimage

source = np.array(Image.open('lena.png'))

# colorDim3List = np.dsplit(source, 3)
# red = colorDim3List[0].reshape(source.shape[0], source.shape[1])
# green = colorDim3List[1].reshape(source.shape[0], source.shape[1])
# blue = colorDim3List[2].reshape(source.shape[0], source.shape[1])

modeList = ['reflect', 'grid-mirror', 'constant', 'grid-constant', 'nearest', 'mirror', 'grid-wrap', 'wrap']
for mode in modeList:
    target = ndimage.shift(source, (30, 100, 0), mode=mode)
    Image.fromarray(target).save('shift_' + mode + '.png')