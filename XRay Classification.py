import cv2 as cv
import skimage
from matplotlib import pyplot as plt
img = cv.imread('histeq_numpy1.jpeg',0)
img2 = cv.equalizeHist(img)
cv.imwrite('histeq_numpy2.jpeg',img2)