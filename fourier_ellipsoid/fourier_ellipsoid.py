import numpy as np
from PIL import Image
import scipy.ndimage as ndimage

source = np.array(Image.open('lena.png'))

colorDim3List = np.dsplit(source, 3)
red = colorDim3List[0].reshape(source.shape[0], source.shape[1])
green = colorDim3List[1].reshape(source.shape[0], source.shape[1])
blue = colorDim3List[2].reshape(source.shape[0], source.shape[1])

def fourier_ellipsoid(red, green, blue, size):
    redFourierEllipsoid = np.fft.ifft2(ndimage.fourier_ellipsoid(red, size=size)).real.astype(np.uint8)
    greenFourierEllipsoid = np.fft.ifft2(ndimage.fourier_ellipsoid(green, size=size)).real.astype(np.uint8)
    blueFourierEllipsoid =  np.fft.ifft2(ndimage.fourier_ellipsoid(blue, size=size)).real.astype(np.uint8)
    return np.dstack((redFourierEllipsoid, greenFourierEllipsoid, blueFourierEllipsoid))

varrays = []
harrays = []
for i in range(1001, 1010):
    fourier_ellipsoid3D = fourier_ellipsoid(red, green, blue, i)
    harrays.append(fourier_ellipsoid3D)
    if i % 3 == 0:
        varrays.append(np.hstack(harrays))
        harrays = []
        
full3D = np.vstack(varrays)
Image.fromarray(full3D).save('fourier_ellipsoid.png')