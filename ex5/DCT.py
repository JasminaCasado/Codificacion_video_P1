# Import functions and libraries
import numpy as np
import matplotlib.pyplot as plt
import scipy

from numpy import pi
from numpy import sin
from numpy import zeros
from numpy import r_
from scipy import signal
from scipy import fftpack
from scipy import misc  # pip install Pillow
import matplotlib.pylab as pylab

# matplotlib inline
# pylab.rcParams['figure.figsize'] = (20.0, 7.0)

im = plt.imread("Lenna.png").astype(float)  # we load a png image


def dct2(a):
    return scipy.fftpack.dct(scipy.fftpack.dct(a, axis=0, norm='ortho'), axis=1, norm='ortho')


def idct2(a):
    return scipy.fftpack.idct(scipy.fftpack.idct(a, axis=0, norm='ortho'), axis=1, norm='ortho')


imsize = im.shape
dct = np.zeros(imsize)

# Do 8x8 DCT on image (in-place)
for i in r_[:imsize[0]:8]:
    for j in r_[:imsize[1]:8]:
        dct[i:(i + 8), j:(j + 8)] = dct2(im[i:(i + 8), j:(j + 8)])

# Display entire DCT
plt.figure()
plt.imshow(dct, cmap='gray', vmax=np.max(dct) * 0.01, vmin=0)
plt.title("8x8 DCTs of the image")
plt.show()

# Threshold
thresh = 0.012
dct_thresh = dct * (abs(dct) > (thresh * np.max(dct)))
percent_nonzeros = np.sum(dct_thresh != 0.0) / (imsize[0] * imsize[1] * 1.0)

print("Keeping only %f%% of the DCT coefficients" % (percent_nonzeros * 100.0))

im_dct = np.zeros(imsize)

for i in r_[:imsize[0]:8]:
    for j in r_[:imsize[1]:8]:
        im_dct[i:(i + 8), j:(j + 8)] = idct2(dct_thresh[i:(i + 8), j:(j + 8)])

plt.figure()
plt.imshow(np.hstack((im, im_dct)), cmap='gray')
plt.title("Comparison between original and DCT compressed images")
plt.show()
