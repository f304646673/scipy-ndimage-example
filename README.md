# 滤镜
在[《使用numpy处理图片——模糊处理》](https://blog.csdn.net/breaksoftware/article/details/135512428)一文中，我们介绍了如何使用scipy库进行滤镜处理。本文我们将通过9宫格的形式，展现不同参数时滤镜效果。
## black_tophat

```python
import sys 
sys.path.append("..") 
from frame import *
import scipy.ndimage as ndimage

generate('lena.png', 'black_tophat.png', ndimage.black_tophat, 1, 91, 10)
```
对应的size（ndimage.black_tophat第二个参数）的值
|  1|11  |21 |
|--|--|--|
| 31 |41  |51 |
| 61 |71  |81 | 

![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/c4052dcc99d547d1be1838492e9a6899.png#pic_center)

## white_tophat 

```python
import sys 
sys.path.append("..") 
from frame import *
import scipy.ndimage as ndimage

def func(*args):
    return ndimage.white_tophat(args[0], args[1])

generate('lena.png', 'white_tophat.png', func, 1, 91, 10)
```

对应的size（ndimage.white_tophat第二个参数）的值
|  1|11  |21 |
|--|--|--|
| 31 |41  |51 |
| 61 |71  |81 | 

![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/4c2a4030505b4bb88b6e8eb75964596e.png#pic_center)

## convolve

```python
import sys 
sys.path.append("..") 
from frame import *
import scipy.ndimage as ndimage

def func(*args):
    weights = np.eye(args[1])
    return ndimage.convolve(args[0], weights)

generate('lena.png', 'convolve.png', func, 1, 10, 1)
```

对应的weights（ndimage.convolve第二个参数）的维度是
|  1|2  |3 |
|--|--|--|
|  4| 5 |6 |
| 7 |8  |9 | 

![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/53e9fa38bbac49818d1ae03b3d6553ec.png#pic_center)

## correlate

```python
import sys 
sys.path.append("..") 
from frame import *
import scipy.ndimage as ndimage

def func(*args):
    weights = np.eye(args[1])
    return ndimage.correlate(args[0], weights)

generate('lena.png', 'correlate.png', func, 1, 10, 1)
```

对应的weights（ndimage.correlate第二个参数）的维度是
|  1|2  |3 |
|--|--|--|
|  4| 5 |6 |
| 7 |8  |9 | 

![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/162d1a0e0f1e46999d6780a44dabe8e0.png#pic_center)

## gaussian_filter

```python
import sys 
sys.path.append("..") 
from frame import *
import scipy.ndimage as ndimage

generate('lena.png', 'gaussian_filter.png', ndimage.gaussian_filter, 1, 10, 1)
```

对应的sigma（ndimage.gaussian_filter第二个参数）的值
|  1|2  |3 |
|--|--|--|
|  4| 5 |6 |
| 7 |8  |9 | 

![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/ad141b3539764fb98729d79d25e077ae.png#pic_center)

## gaussian_laplace

```python
import sys 
sys.path.append("..") 
from frame import *
import scipy.ndimage as ndimage

generate('lena.png', 'gaussian_laplace.png', ndimage.gaussian_laplace, 0.2, 1.9, 0.2)
```

对应的sigma（ndimage.black_tophat第二个参数）的值
|  0.2|0.4  |0.6 |
|--|--|--|
|  0.8| 1.0 |1.2 |
| 1.4 |1.6  |1.8 | 

![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/cb7d55edf2754d9e9e100f34bd10c6d6.png#pic_center)

## maximum_filter

```python
import sys 
sys.path.append("..") 
from frame import *
import scipy.ndimage as ndimage

generate('lena.png', 'maximum_filter.png', ndimage.maximum_filter, 1, 10, 1)
```

对应的size（ndimage.maximum_filter第二个参数）的值
|  1|2  |3 |
|--|--|--|
|  4| 5 |6 |
| 7 |8  |9 | 

![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/e350eca19a734f88b9c7c824dff1a7ee.png#pic_center)

## median_filter

```python
import sys 
sys.path.append("..") 
from frame import *
import scipy.ndimage as ndimage

generate('lena.png', 'median_filter.png', ndimage.median_filter, 1, 10, 1)
```

对应的size（ndimage.median_filter第二个参数）的值
|  1|2  |3 |
|--|--|--|
|  4| 5 |6 |
| 7 |8  |9 | 

![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/18ec89bc4c46427f92bd1a7ea35d8c62.png#pic_center)

## minimum_filter

```python
import sys 
sys.path.append("..") 
from frame import *
import scipy.ndimage as ndimage

generate('lena.png', 'minimum_filter.png', ndimage.minimum_filter, 1, 10, 1)
```

对应的size（ndimage.minimum_filter第二个参数）的值
|  1|2  |3 |
|--|--|--|
|  4| 5 |6 |
| 7 |8  |9 | 

![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/b5455c21b0644aa5bba747501a87083b.png#pic_center)

## percentile_filter

```python
import sys 
sys.path.append("..") 
from frame import *
import scipy.ndimage as ndimage

def func(*args):
    return ndimage.percentile_filter(args[0], percentile=args[1], size=args[1])

generate('lena.png', 'percentile_filter.png', func, 1, 10, 1)
```

对应的percentile和size（ndimage.percentile_filter第二、三个参数）的值
|  1|2  |3 |
|--|--|--|
|  4| 5 |6 |
| 7 |8  |9 | 

![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/82cb2cbdb3e94f1db8ce00f957d1b61d.png#pic_center)

## prewitt

```python
import sys 
sys.path.append("..") 
from frame import *
import scipy.ndimage as ndimage

def func(*args):
    return ndimage.prewitt(args[0])

generate('lena.png', 'prewitt.png', func, 1, 2, 1)
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/8b5ba357a71f4e3c814f70c13b945b33.png#pic_center)

## rank_filter

```python
import sys 
sys.path.append("..") 
from frame import *
import scipy.ndimage as ndimage

def func(*args):
    return ndimage.rank_filter(args[0], rank=args[1], size=args[1]*2)

generate('lena.png', 'rank_filter.png', func, 1, 10, 1)
```

对应的rank（ndimage.rank_filter第二个参数）的值
|  1|2  |3 |
|--|--|--|
|  4| 5 |6 |
| 7 |8  |9 | 	

对应的size（ndimage.rank_filter第三个参数）的值
|  2|4 |6 |
|--|--|--|
|  8| 10 |12 |
| 14 |16  |18 | 


![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/30919d0811524d959586f55f3a00bbf4.png#pic_center)

## sobel

```python
import sys 
sys.path.append("..") 
from frame import *
import scipy.ndimage as ndimage

def func(*args):
    return ndimage.sobel(args[0])

generate('lena.png', 'sobel.png', func, 1, 2, 1)
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/55ab6fc6c82b42528adcdefb3c4a784e.png#pic_center)

## spline_filter

```python
import sys 
sys.path.append("..") 
from frame import *
import scipy.ndimage as ndimage

def func(*args):
    return ndimage.spline_filter(args[0], args[1]).astype(np.uint8)

generate('lena.png', 'spline_filter.png', func, 2, 5, 1)
```

对应的size（ndimage.black_tophat第二个参数）的值
|  2|3  |4 |
|--|--|--|

![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/acfb76b74ad7492bad7c070c10f8e1f5.png#pic_center)

## uniform_filter

```python
import sys 
sys.path.append("..") 
from frame import *
import scipy.ndimage as ndimage

def func(*args):
    return ndimage.uniform_filter(args[0], args[1])

generate('lena.png', 'uniform_filter.png', func, 1, 10, 1)
```

对应的size（ndimage.uniform_filter第二个参数）的值
|  1|2  |3 |
|--|--|--|
|  4| 5 |6 |
| 7 |8  |9 | 

![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/93500d3931f7491d9654f5f9596b8e28.png#pic_center)

## 基础代码

```python
# frame.py
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
```

## 代码仓库
[https://github.com/f304646673/scipy-ndimage-example/tree/main/](https://github.com/f304646673/scipy-ndimage-example/tree/main/)

# 缩放
在[《使用numpy处理图片——缩放图片》](https://blog.csdn.net/breaksoftware/article/details/135542028)一文中，我们每2个取1个像素来达到图像缩小的效果。这就要求缩小的比例只能是整数倍，而不能支持缩小到0.3倍或者放大到1.5倍这样的效果。
为了支持任意倍数的缩放功能，我们需要使用scipy的zoom方法。
先看下原图
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/ea0ebf6c4cf340958fa0a709f96d068d.png#pic_center)

```python
import numpy as np
from PIL import Image
import scipy.ndimage as ndimage

img = Image.open('lena.png')
data = np.array(img)
```

## 缩小
下面的代码是对第一、二轴都缩小到原来的0.3倍，而第三轴是颜色，不做任何变化。
```python
img03 = ndimage.zoom(data, zoom=(0.3, 0.3, 1))
Image.fromarray(img03).save('zoom03.png')
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/173512f8043647249a96d1de3f0a0d8f.png#pic_center)

## 放大
下面的代码是对第一、二轴都放大到原来的1.5倍，而第三轴是颜色，不做任何变化。
```python
img15 = ndimage.zoom(data, zoom=(1.5, 1.5, 1))
Image.fromarray(img15).save('zoom15.png')
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/58ea53ba3ded45cb9d6ebd742f33682c.png#pic_center)
## 代码地址
[https://github.com/f304646673/scipy-ndimage-example/tree/main/zoom](https://github.com/f304646673/scipy-ndimage-example/tree/main/zoom)

# 旋转
在[《使用numpy处理图片——90度旋转》](https://blog.csdn.net/breaksoftware/article/details/135534921)中，我们使用numpy提供的方法，可以将矩阵旋转90度。而如果我们需要旋转任意角度，则需要自己撸很多代码。如果我们使用scipy库提供的方法，则会容易很多。
需要注意的是，旋转导致原始的图片会“撑开”修改后的图片大小。当然我们也可以通过参数设置，让图片大小不变，但是会让部分图片显示不出来。

## 载入图片

```python
import numpy as np
import PIL.Image as Image
import scipy.ndimage as ndimage

data = np.array(Image.open('the_starry_night.jpg'))
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/cb204335469245058b578ff2c0c8a771.jpeg#pic_center)

## 左旋转30度，且重新调整图片大小

```python
left30 = ndimage.rotate(data, 30)

Image.fromarray(left30).save('left30.png')
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/f9069738c900413da7bd1640cbf251ce.png#pic_center)


## 右旋转30度，且重新调整图片大小

```python
right30 = ndimage.rotate(data, -30)

Image.fromarray(right30).save('right30.png')
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/41c5b64be48f467c9f35460cd6518933.png#pic_center)
## 左旋转135度，保持图片大小不变
注意我们给reshape参数传递了False，即不调整图片大小
```python
left135 = ndimage.rotate(data, 135, reshape=False)

Image.fromarray(left135).save('left135.png')
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/e309c52629f9425ab3be1277ef670d44.png#pic_center)

## 右旋转135度，保持图片大小不变

```python
right135 = ndimage.rotate(data, -135, reshape=False)

Image.fromarray(right135).save('right135.png')
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/04f04798e5d54f9ab4f5c852306779f6.png#pic_center)
## 代码地址
[https://github.com/f304646673/scipy-ndimage-example/tree/main/rot](https://github.com/f304646673/scipy-ndimage-example/tree/main/rot)
