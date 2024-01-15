import numpy as np
from PIL import Image
import scipy.ndimage as ndimage

source = np.array(Image.open('lena.png'))

colorDim3List = np.dsplit(source, 3)
red = colorDim3List[0].reshape(source.shape[0], source.shape[1])
green = colorDim3List[1].reshape(source.shape[0], source.shape[1])
blue = colorDim3List[2].reshape(source.shape[0], source.shape[1])

def rank_filter(red, green, blue, rank):
    redRankFilter =  ndimage.rank_filter(red, rank=rank, size=rank*2)
    greenRankFilter = ndimage.rank_filter(green, rank=rank, size=rank*2)
    blueRankFilter =  ndimage.rank_filter(blue, rank=rank, size=rank*2)
    return np.dstack((redRankFilter, greenRankFilter, blueRankFilter))

varrays = []
harrays = []
for i in range(1, 10):
    rank_filter3D = rank_filter(red, green, blue, i)
    harrays.append(rank_filter3D)
    if i % 3 == 0:
        varrays.append(np.hstack(harrays))
        harrays = []
        
full3D = np.vstack(varrays)
Image.fromarray(full3D).save('rank_filter.png')