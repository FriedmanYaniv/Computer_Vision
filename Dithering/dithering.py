import numpy as np
import os
import cv2
import matplotlib.pyplot as plt


# load image
img_path = r'C:\Users\yaniv\PycharmProjects\WSC-sports\assorted_tomatoes.jpg'
img = cv2.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(img, cmap='gray')
plt.title('original')
height, width = img.shape


# dithering kernel
d_kern = np.array([[64, 128], [192, 0]])
fact = 2
dithered = np.zeros((height, width))

# fill dithered image
for i in range(int(height/fact)):
    for j in range(int(width/fact)):
        curr_window = img[i*fact: i*fact+2, j*fact: j*fact+2]
        dithered[i*fact: i*fact+2, j*fact: j*fact+2] = (curr_window > d_kern).astype('int')


# plot
plt.figure()
plt.imshow(dithered, cmap='gray')
plt.title('dithered')
