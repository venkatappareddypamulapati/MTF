import cv2
import numpy as np
import skimage
import matplotlib.pyplot as plt
from numpy import random
#from skimage.util import random_noise
#img=cv2.imread('/home/venkat/Downloads/ROI_Selection.png')
#img=cv2.imread('/home/venkat/Downloads/Exact_45.tif')
#img=cv2.imread('/home/venkat/Downloads/slant.png')
#img=cv2.imread('/home/venkat/Test_Images/img.tif', 0)
img=cv2.imread('/home/venkat/data_set1/img6.png', cv2.IMREAD_UNCHANGED)
img=cv2.imread('/home/venkat/data_set1/img6.png', 0)
#img=skimage.img_as_float(img)
#img=img[:,:,1]
print(img.shape)
#np.random.seed(40)
#noise=np.random.normal(0,.1,img.shape)
noise=255*random.poisson(lam=.01, size=img.shape)
img_noise=img+noise
#img_noise=img
plt.imshow(img_noise, cmap='gray')
plt.show()
print(np.std(img_noise))
print(img_noise.shape)
#img=np.float64(img)
#blur=cv2.GaussianBlur(img, (7, 7), 0)
#np.random.seed(0)
#gauss = np.random.normal(0, 1, img.shape)

# Add noise to the image
#noisy_img = img + 10 * gauss

#blur = random_noise(img, mode='s&p', seed=None, clip=True)

cv2.imwrite('/home/venkat/Downloads/noisy.png', img_noise)
#print(img)
#cv2.imwrite('/home/venkat/Downloads/blurred.tif', blur)