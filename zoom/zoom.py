import numpy as np
from PIL import Image
import scipy.ndimage as ndimage

img = Image.open('lena.png')
data = np.array(img)

img03 = ndimage.zoom(data, zoom=(0.3, 0.3, 1))
Image.fromarray(img03).save('zoom03.png')

img15 = ndimage.zoom(data, zoom=(1.5, 1.5, 1))
Image.fromarray(img15).save('zoom15.png')

# colorDim3List = np.dsplit(data, 3)
# red = colorDim3List[0].reshape((data.shape[0], data.shape[1]))
# green = colorDim3List[1].reshape((data.shape[0], data.shape[1]))
# blue = colorDim3List[2].reshape((data.shape[0], data.shape[1]))

# redZoom03 = ndimage.zoom(red, zoom=0.3)
# greenZoom03 = ndimage.zoom(green, zoom=0.3)
# blueZoom03 = ndimage.zoom(blue, zoom=0.3)

# zoom03 = np.dstack((redZoom03, greenZoom03, blueZoom03))
# Image.fromarray(zoom03).save('zoom03.png')

# redZoom15 = ndimage.zoom(red, zoom=1.5)
# greenZoom15 = ndimage.zoom(green, zoom=1.5)
# blueZoom15 = ndimage.zoom(blue, zoom=1.5)

# zoom15 = np.dstack((redZoom15, greenZoom15, blueZoom15))
# Image.fromarray(zoom15).save('zoom15.png')