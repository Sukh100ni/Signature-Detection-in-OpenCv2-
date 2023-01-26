# -*- coding: utf-8 -*-
"""Final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q0JeL74Vsys4ZZBfFjrd4yZnfywdF06E

**Read an image**
"""

import numpy as np 
import cv2
img=cv2.imread("/content/sign.jpeg")

print(img)

"""**Display an image**"""

from google.colab.patches import cv2_imshow
cv2_imshow(img)

"""**Gray Scale image**"""

import numpy as np 
import cv2
img=cv2.imread("/content/sign.jpeg",0)

print(img)

from google.colab.patches import cv2_imshow
cv2_imshow(img)

cv2.imwrite('save_img.png',img)

"""**Resize an image**"""

import cv2
import numpy as np

FILE_NAME = '/content/sign.jpeg'
try:
	# Read image from disk.
	img = cv2.imread(FILE_NAME)

	# Get number of pixel horizontally and vertically.
	(height, width) = img.shape[:2]

	# Specify the size of image along with interpolation methods.
	# cv2.INTER_AREA is used for shrinking, whereas cv2.INTER_CUBIC
	# is used for zooming.
	res = cv2.resize(img, (int(width / 2), int(height / 2)), interpolation = cv2.INTER_CUBIC)

	# Write image back to disk.
	cv2.imwrite('result.jpeg', res)
except IOError:
	print ('Error while reading files !!!')

print(res)

from google.colab.patches import cv2_imshow
cv2_imshow(res)

print(img.dtype)
print(img.shape)
print(img.size)

"""**Automatic crop**




"""

import cv2
import numpy as np
 
img = cv2.imread('/content/result.jpeg')
print(img.shape) # Print image shape
from google.colab.patches import cv2_imshow
cv2_imshow(img)
 
# Cropping an image
cropped_image = img[100:300, 150:400]
 
# Display cropped image
from google.colab.patches import cv2_imshow
cv2_imshow(cropped_image)
 
# Save the cropped image
cv2.imwrite("Cropped Image.jpg", cropped_image)
 
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
img = cv2.imread('/content/sign.jpeg')

y=0
x=0
h=700
w=900
crop_img = img[x:w, y:h]
from google.colab.patches import cv2_imshow
cv2_imshow(crop_img)
cv2.waitKey(0)

"""


**Corner  Detection**"""

# import the required library
import numpy as np
import cv2
from matplotlib import pyplot as plt
# read the image
img = cv2.imread('/content/result.jpeg')
# convert image to gray scale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# detect corners with the goodFeaturesToTrack function.
corners = cv2.goodFeaturesToTrack(gray, 27, 0.01, 10)
corners = np.int0(corners)
# we iterate through each corner,
# making a circle at each point that we think is a corner.
for i in corners:
	x, y = i.ravel()
	cv2.circle(img, (x, y), 3, 255, -1)
plt.imshow(img), plt.show()

"""**Edge Detection**"""

import cv2
import numpy as np

FILE_NAME = '/content/result.jpeg'
try:
	# Read image from disk.
	img = cv2.imread(FILE_NAME)

	# Canny edge detection.
	edges = cv2.Canny(img, 100, 200)

	# Write image back to disk.
	cv2.imwrite('result.jpeg 1', edges)
except IOError:
	print ('Error while reading files')

print(edges)

from google.colab.patches import cv2_imshow
cv2_imshow(edges)

# Canny Edge Detection.
import cv2
import numpy as np
import glob
import os
from matplotlib import pyplot as plt
from PIL import Image

DIR_PATH ='/content/result.jpeg'

# Read all images.
all_files_dir = glob.glob(DIR_PATH)

for file_item in all_files_dir:
    try:
        # Read image from disk.
        img = cv2.imread(file_item)

        # Canny edge detection.
        edges = cv2.Canny(img, 100, 200)

        filename = os.path.basename(file_item).split('.')[0]
        cv2.imwrite(filename + '_l.jpg', edges)
    except IOError:
        print ('Error while reading files!!!')

print(edges)

from google.colab.patches import cv2_imshow
cv2_imshow(edges)

""" **SIFT** 
 
 Using the simple draw keypoints in image with flag value  zero

"""

# import required libraries
import cv2

# read input image
img = cv2.imread('/content/result.jpeg')

# convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Initiate SIFT object with default values
sift = cv2.SIFT_create()

# find the keypoints on image (grayscale)
kp = sift.detect(gray,None)

# draw keypoints in image
img2 = cv2.drawKeypoints(gray, kp, None, flags=0)

# display the image with keypoints drawn on it
from google.colab.patches import cv2_imshow
cv2_imshow(img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""**SIFT**  
To draw rich keypoints  in an Signature image with flag 
"""

# import required libraries
import cv2

# read input image
img = cv2.imread('/content/result.jpeg')

# convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Initiate SIFT object with default values
sift = cv2.SIFT_create()

# find the keypoints on image (grayscale)
kp = sift.detect(gray,None)

# draw keypoints in image
img2=cv2.drawKeypoints(gray,kp,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# display the image with keypoints drawn on it
from google.colab.patches import cv2_imshow
cv2_imshow(img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""**SURF**"""

import numpy as np
import cv2 as cv
ori =cv.imread('/content/result.jpeg')
img = cv.imread('/content/result.jpeg')

surf = cv.xfeatures2d.SURF_create(400)
kp, des = surf.detectAndCompute(img,None)
img2 = cv.drawKeypoints(img,kp,None,(255,0,0),4)
cv.imshow('Original', ori)
cv.imshow('SURF', img2)

