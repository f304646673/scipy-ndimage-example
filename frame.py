import numpy as np
from PIL import Image
import scipy.ndimage as ndimage

def generate(image_from, image_to, filter, start = 1, end = 10, step = 1):
    source = np.array(Image.open(image_from))

    colorDim3List = np.dsplit(source, 3)
    red = colorDim3List[0].reshape(source.shape[0], source.shape[1])
    green = colorDim3List[1].reshape(source.shape[0], source.shape[1])
    blue = colorDim3List[2].reshape(source.shape[0], source.shape[1])

    def inline_filter(red, green, blue, some_value):
        redFilter = filter(red, some_value)
        greenFilter = filter(green, some_value)
        blueFilter = filter(blue, some_value)
        return np.dstack((redFilter, greenFilter, blueFilter))

    varrays = []
    harrays = []
    hindex = 0
    for i in np.arange(start, end, step):
        filter3D = inline_filter(red, green, blue, i)
        harrays.append(filter3D)
        hindex += 1
        if hindex % 3 == 0:
            varrays.append(np.hstack(harrays))
            harrays = []
            hindex = 0
            
    if varrays == []:
        varrays.append(np.hstack(harrays))
            
    full3D = np.vstack(varrays)
    Image.fromarray(full3D).save(image_to)