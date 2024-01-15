import numpy as np
from PIL import Image
import scipy.ndimage as ndimage

source = np.array(Image.open('lena.png'))

varrys = []
harrys = []
for i in range(1, 10):
    gaussianGradientMagnitude = ndimage.gaussian_gradient_magnitude(source, sigma=i)
    harrys.append(gaussianGradientMagnitude)
    if i % 3 == 0:
        varrys.append(np.hstack(harrys))
        harrys = []
        
full = np.vstack(varrys)
Image.fromarray(full).save('gaussian_gradient_magnitude.png')

# colorDim3List = np.dsplit(source, 3)
# red = colorDim3List[0].reshape(source.shape[0], source.shape[1])
# green = colorDim3List[1].reshape(source.shape[0], source.shape[1])
# blue = colorDim3List[2].reshape(source.shape[0], source.shape[1])

# def gaussian_gradient_magnitude(red, green, blue, sigma):
#     redGaussianGradientMagnitude =  ndimage.gaussian_gradient_magnitude(red, sigma=sigma)
#     greenGaussianGradientMagnitude = ndimage.gaussian_gradient_magnitude(green, sigma=sigma)
#     blueGaussianGradientMagnitude =  ndimage.gaussian_gradient_magnitude(blue, sigma=sigma)
#     return np.dstack((redGaussianGradientMagnitude, greenGaussianGradientMagnitude, blueGaussianGradientMagnitude))

# varrays = []
# harrays = []
# for i in range(1, 10):
#     gaussianGradientMagnitude3D = gaussian_gradient_magnitude(red, green, blue, i)
#     harrays.append(gaussianGradientMagnitude3D)
#     if i % 3 == 0:
#         varrays.append(np.hstack(harrays))
#         harrays = []
        
# full3D = np.vstack(varrays)
# Image.fromarray(full3D).save('gaussian_gradient_magnitude.png')
