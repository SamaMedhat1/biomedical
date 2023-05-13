import imageio.v2 as imageio
from sympy.codegen.fnodes import cmplx
import scipy.ndimage as ndi
import matplotlib.pyplot as plt
import numpy as np


#dicom_dir
#ID_0034_AGE_0061_CONTRAST_1_CT.dcm
class ImageAnalysis:

    image = imageio.imread("dicom_dir/ID_0046_AGE_0072_CONTRAST_1_CT.dcm")

    def segmentObjects(self):
          plt.imshow(self.image, cmap='gray')
          plt.show()
          im_filt = ndi.median_filter(self.image, size=11)
          mask_start = np.where(im_filt > 60, 1, 0)
          mask = ndi.binary_closing(mask_start)
          labels, nlabels = ndi.label(mask)
          print('Num. Labels:', nlabels)
          overlay = np.where(labels > 0, labels,
                             np.nan)
          plt.imshow(overlay, cmap='rainbow')
          #plt.axis('off')
          plt.show()
          return labels

    def extractCancer(self, labels):
        bboxes = ndi.find_objects(labels == 2)
        print('Number of objects:', len(bboxes))
        print('Indices for first box:',
              bboxes[0])
        # Crop to the left ventricle (index 0)
        im_lv = self.image[bboxes[0]]
        # Plot the cropped image
        plt.imshow(im_lv)
        plt.axis('off')
        plt.show()
        hist = ndi.histogram(im_lv, min=0,
                             max=255, bins=256)
        plt.plot(hist)
        plt.suptitle("Histogram")
        plt.show()

def _main_():
    i = ImageAnalysis()
    labels = i.segmentObjects()
    i.extractCancer(labels)

_main_()


