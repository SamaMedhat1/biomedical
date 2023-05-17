import imageio.v2 as imageio
import scipy.ndimage as ndi
import matplotlib.pyplot as plt
import numpy as np


# dicom_dir
# ID_0034_AGE_0061_CONTRAST_1_CT.dcm
class ImageAnalysis:
    image = imageio.imread("dicom_dir/ID_0046_AGE_0072_CONTRAST_1_CT.dcm")

    def segment_objects(self):
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
        # plt.axis('off')
        plt.show()
        return labels

    def extract_cancer(self, labels):
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

    def calc_area(self, labels):
        d1, d2 = self.image.meta['sampling']
        dimension_of_pixels = d1 * d2
        # Count label pixels
        num_of_pixels = ndi.sum(1, labels, index=2)
        # Calculate volume of label
        area = num_of_pixels * dimension_of_pixels
        print("the area is = ", area)

    def distance_transformation(self, labels):
        # the distance In terms of background
        mask = np.where(labels == 2, 1, 0)
        d = ndi.distance_transform_edt(mask)
        print("the distance In terms of background = ", d.max())

    def center_mass(self, labels):
        coms = ndi.center_of_mass(self.image, labels, index=2)
        print('the center :', coms)

    def thresholding(self, thershold):
        return self.image > thershold

    def print_image(self, image):
        plt.imshow(image, cmap='gray')
        plt.axis('off')
        plt.show()

    def apply_morphological_operation(self):
        mask = self.image > 2
        self.print_image(mask)

        # noise reduction
        mask = ndi.binary_erosion(mask, iterations=2)
        mask = ndi.binary_dilation(mask, iterations=2)
        self.print_image(mask)

        # fill gaps
        mask = ndi.binary_dilation(mask, iterations=25)
        mask = ndi.binary_erosion(mask, iterations=25)
        self.print_image(mask)

        return mask

    def print_histogram(self, image):
        hist = ndi.histogram(image, min=0,
                             max=255, bins=256)
        plt.plot(hist)
        plt.suptitle("Histogram")
        plt.show()

    def feature_detection(self):
        weights = [[+1, 0, -1], [+1, 0, -1], [+1, 0, -1]]

        return ndi.convolve(self.image, weights)

    def edge_detection(self):
        sobel_ax0 = ndi.sobel(self.image, axis=0)
        sobel_ax1 = ndi.sobel(self.image, axis=1)

        edges = np.sqrt(np.square(sobel_ax0) +
                        np.square(sobel_ax1))
        return edges


'''
def _main_():
    i = ImageAnalysis()
    
    labels = i.segment_objects()
    i.extract_cancer(labels)
    i.calc_area(labels)
    i.distance_transformation(labels)
    i.center_mass(labels)
    
    # point one / task 2
    image = i.image
    i.print_image(image)
    i.print_histogram(image)

    mask = i.apply_morphological_operation()
    new_image = mask * image
    i.print_image(new_image)
    i.print_histogram(new_image)

    # point two/ task 2
    feature = i.feature_detection()
    i.print_image(feature)
    edges = i.edge_detection()
    i.print_image(edges)


_main_()
'''
