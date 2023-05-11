import imageio.v2 as imageio
from sympy.codegen.fnodes import cmplx
import scipy.ndimage as ndi
import matplotlib.pyplot as plt
import numpy as np


#dicom_dir
class ImageAnalysis:

    image = imageio.imread("dicom_dir/ID_0091_AGE_0072_CONTRAST_0_CT.dcm")

    def segment(self):
        plt.imshow(self.image, cmap='gray')
        img_filter = ndi.median_filter(self.image, size=3)
        mask = np.where(img_filter > 2, 1, 0)
        mask = ndi.binary_closing(mask)
        labels, nlabels = ndi.label(mask)
        print('Num. Labels:', nlabels)
        overlay = np.where(labels > 0, labels, np.nan)
        plt.imshow(overlay, cmap='rainbow')
        # plt.axis('off')
        # plt.show()
        return labels

    def extract_object(self,label):
        bboxes = ndi.find_objects(label == 5)
        # Crop to the left ventricle (index 0)
        print('Number of objects:', len(bboxes))
        print('Indices for first box:',
              bboxes[0])
        # Crop to the left ventricle (index 0)
        im_lv = self.image[bboxes[0]]
        # Plot the cropped image
        plt.imshow(im_lv)




def _main_():

    i = ImageAnalysis()
    l = i.segment()
    i.extract_object(l)


_main_()