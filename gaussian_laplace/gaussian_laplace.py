import numpy as np
from PIL import Image
import scipy.ndimage as ndimage

source = np.array(Image.open('lena.png'))

# varrys = []
# harrys = []
# for i in range(1, 10):
#     gaussianLaplace = ndimage.gaussian_laplace(source, sigma=i)
#     harrys.append(gaussianLaplace)
#     if i % 3 == 0:
#         varrys.append(np.hstack(harrys))
#         harrys = []
        
# full = np.vstack(varrys)
# Image.fromarray(full).save('gaussian_laplace.png')

colorDim3List = np.dsplit(source, 3)
red = colorDim3List[0].reshape(source.shape[0], source.shape[1])
green = colorDim3List[1].reshape(source.shape[0], source.shape[1])
blue = colorDim3List[2].reshape(source.shape[0], source.shape[1])

def gaussian_laplace(red, green, blue, sigma):
    redGaussianLaplace =  ndimage.gaussian_laplace(red, sigma=sigma)
    greenGaussianLaplace = ndimage.gaussian_laplace(green, sigma=sigma)
    blueGaussianLaplace =  ndimage.gaussian_laplace(blue, sigma=sigma)
    return np.dstack((redGaussianLaplace, greenGaussianLaplace, blueGaussianLaplace))

varrays = []
harrays = []
for i in range(1, 10):
    gaussian_laplace3D = gaussian_laplace(red, green, blue, i)
    harrays.append(gaussian_laplace3D)
    if i % 3 == 0:
        varrays.append(np.hstack(harrays))
        harrays = []
        
full3D = np.vstack(varrays)
Image.fromarray(full3D).save('gaussian_laplace.png')