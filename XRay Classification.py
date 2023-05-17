import cv2 as cv
import skimage
from matplotlib import pyplot as plt
img = cv.imread('Tornier.65.jpg',0)
img2 = cv.equalizeHist(img)*255
cv.imwrite('histeq_numpy1.jpeg',img2)