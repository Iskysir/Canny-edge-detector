from __future__ import division
from numpy import array, zeros, abs
from numpy.fft import fft2, ifft2
from PIL import Image
from matplotlib.pyplot import imshow, show, subplot, figure, gray, title

def gaussian(im):
    b = array([[2, 4,  5,  2,  2],
               [4, 9,  12, 9,  4],
               [5, 12, 15, 12, 5],
               [4, 9,  12, 9,  4],
               [2, 4,  5,  4,  2]]) / 156;
    kernel = zeros(im.shape)
    kernel[:b.shape[0], :b.shape[1]] = b

    fim = fft2(im)
    fkernel = fft2(kernel)
    fil_im = ifft2(fim * fkernel)

    return abs(fil_im).astype(int)

im = array(Image.open("emilia.jpg"))
im = im[:, :, 0]
gray()

subplot(1, 2, 1)
imshow(im)
title('Original')

subplot(1, 2, 2)
imshow(gaussian(im))
title('Filtered')

show()
