import cv2
import numpy as np
import skimage
import matplotlib.pyplot as plt
#from skimage.util import random_noise
#img=cv2.imread('/home/venkat/Downloads/ROI_Selection.png')
#img=cv2.imread('/home/venkat/Downloads/Exact_45.tif')
#img=cv2.imread('/home/venkat/Downloads/slant.png')
img=cv2.imread('/home/venkat/Test_Images/img2.tif', 0)
img=skimage.img_as_float(img)
#np.random.seed(40)
gauss=np.random.normal(0,1,img.shape)
img_gauss=img+1*gauss
plt.imshow(img_gauss)
plt.show()

#img=np.float64(img)
#blur=cv2.GaussianBlur(img, (7, 7), 0)
#np.random.seed(0)
#gauss = np.random.normal(0, 1, img.shape)

# Add noise to the image
#noisy_img = img + 10 * gauss

#blur = random_noise(img, mode='s&p', seed=None, clip=True)

cv2.imwrite('/home/venkat/Downloads/noisy.tif', img_gauss)
#print(img)

#cv2.imwrite('/home/venkat/Downloads/blurred.tif', blur)