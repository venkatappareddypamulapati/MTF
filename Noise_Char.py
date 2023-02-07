import numpy as np
import skimage
from argparse import ArgumentParser
import os.path
import math
from scipy import signal
import specutils
from specutils.analysis import gaussian_sigma_width, gaussian_fwhm, fwhm, fwzi
import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.widgets import RectangleSelector
from scipy import interpolate
from scipy.signal import savgol_filter
import os, sys
import imutils

# Reference:
# http://stackoverflow.com/questions/6518811/interpolate-nan-values-in-a-numpy-array
def nan_helper(y):
    """Helper to handle indices and logical indices of NaNs."""


    return np.isnan(y), lambda z: z.nonzero()[0]


class EventHandler(object):

    def __init__(self, filename):
        self.filename = filename

    def line_select_callback(self, eclick, erelease):
        'eclick and erelease are the press and release events'
        x1, y1 = eclick.xdata, eclick.ydata
        x2, y2 = erelease.xdata, erelease.ydata
        print('clicked : ',x1, y1, x2, y2)
        self.roi = np.array([y1, y2, x1, x2])
        print('shape of roi : ',self.roi.shape)

    def event_exit_manager(self, event):
        if event.key in ['enter']:
            PDS_Compute_Noise(self.filename, self.roi)

        #elif event.key in ['shift']:
            #Noise_Char(self.filename, self.roi)





class ROI_selection(object):

    def __init__(self, filename):
        self.filename = filename
        self.image_data = cv2.imread(filename,cv2.IMREAD_UNCHANGED)
        fig_image, current_ax = plt.subplots()
        plt.imshow(self.image_data, cmap='gray')
        eh = EventHandler(self.filename)
        rectangle_selector = RectangleSelector(current_ax,
                                               eh.line_select_callback,
                                               useblit=True,
                                               button=[1, 2, 3],
                                               minspanx=10, minspany=10,
                                               spancoords='pixels',
                                               interactive=True)
        plt.connect('key_press_event', eh.event_exit_manager)
        plt.show()

counts=[]
noise_std=[]
class PDS_Compute_Noise(object):

    def __init__(self, filename, roi):
        #image_data = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
        image_data = cv2.imread(filename, 0)
        #image_data = skimage.img_as_float(image_data)
        #gauss = np.random.normal(0, 1, image_data.shape)
        #image_data = image_data + 3 * gauss
        roi = roi.astype(int)
        image_data = image_data[roi[0]:roi[1], roi[2]:roi[3]]
        self.data = image_data

        #np.random.seed()

        print('Data Shape Cropped ROI',self.data.shape)
        self.Noise_Char()
        plt.figure()
        plt.imshow(self.data, cmap='gray')
        plt.show()
        #plt.figure()
        #histr=cv2.calcHist([image_data], [0], None, [256], [0, 256])
        #plt.hist(self.data)
        #plt.show()
        counts_value=np.floor(np.average(self.data[:]))
        print(counts_value)
        counts.append(counts_value)

    def Noise_Char(self):
        std=np.std(self.data)
        #var=nr
        print("Noise Standard Deviation=%f" %(std))
        noise_std.append(std)
if __name__ == '__main__':

    filename="/home/venkat/Downloads/noisy.png"
    #filename = "/home/venkat/data_set1/img10.png"
    ROI_selection(filename)
    print(noise_std)
    print(counts)
    plt.figure()
    plt.plot(counts, noise_std, "*")
    plt.xlabel('Counts')
    plt.ylabel('Noise_Std.')
    plt.title('Counts vs Noise_Std.')
    plt.grid(True)
    plt.show()