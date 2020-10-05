#Task 3 - Histograms
#Transformatino Notes
#Code written by Laura Whelan on 05/10/2020

#==========================================
#This code opens an image which has poor contrast,
#and demonstrates this by displaying its histogram side by side.
#Histogram equalisation is used to improve the contrast of the image
#==========================================

#import the necessary packages:
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui

#1. Open image "wartime.jpg" (and converts from BGR to grayscale)
I = cv2.imread("wartime.jpg")
G = cv2.cvtColor(I , cv2.COLOR_BGR2GRAY)

#2. view its histogram alongside the original image
plt.subplot(2,2,1)
Values = G.ravel()#ravel function converts the image from matrix form to a 1D array
plt.hist(Values, bins=256, range=[0,256])#make the 1D array into a histogram
plt.title('Histogram:Original Image')
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,2)
plt.imshow(G, cmap='gray')
plt.title('Original Image')
plt.xticks([])
plt.yticks([])

#3 use histogram qualisation to improve its contrast and show improved image alongside
plt.subplot(2,2,3)
H= cv2.equalizeHist(G)
Values = H.ravel()
plt.hist(Values, bins=256, range=[0,256])
plt.title('Histogram:Improved Contrast')
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,4)
plt.imshow(H, cmap='gray')
plt.title('Image:Improved Contrast')
plt.xticks([])
plt.yticks([])

#4 show all images
plt.show()