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
        plt.axis('off')
        plt.title("original Image")
        plt.show()
        # Apply median filter
        median_filter = ndi.median_filter(self.image, size=11)
        # show the pixels with intensities greater than 60
        mask = np.where(median_filter > 60, 1, 0)
        # using binary closing
        mask = ndi.binary_closing(mask)
        # using label to return number of objects and array of objects
        labels, num_of_labels = ndi.label(mask)
        print('Num. Labels:', num_of_labels)
        # show all objects in the image
        overlay = np.where(labels > 0, labels, np.nan)
        plt.imshow(overlay, cmap='rainbow')
        plt.axis('off')
        plt.title("segmented Image")
        plt.show()
        return labels

    def extract_cancer(self, labels):
        # Find bounding box
        bounding_boxes = ndi.find_objects(labels == 2)
        print('Number of objects:', len(bounding_boxes))
        print('Indices for first box:',
              bounding_boxes[0])
        # Crop the cancer
        im_crop = self.image[bounding_boxes[0]]
        # Plot the cropped image
        plt.imshow(im_crop)
        plt.axis('off')
        plt.title("Cancer")
        plt.show()
        hist = ndi.histogram(im_crop, min=0,
                             max=255, bins=256)
        plt.plot(hist)
        plt.suptitle("Histogram")
        plt.show()

    def calc_area(self, labels):
        d1, d2 = self.image.meta['sampling']
        dimension_of_pixels = d1 * d2
        # Count label pixels
        num_of_pixels = ndi.sum(1, labels, index=2)
        # Calculate area of label
        area = num_of_pixels * dimension_of_pixels
        print("the area is = ", area)

    def distance_transformation(self, labels):
        # the distance In terms of background
        mask = np.where(labels == 2, 1, 0)
        d = ndi.distance_transform_edt(mask)
        print("the distance In terms of background = ", d.max())

    def center_mass(self, labels):
        center = ndi.center_of_mass(self.image, labels, index=2)
        print('the center :', center)

    def thresholding(self, thershold):
        return self.image > thershold

    def print_image(self, image):
        plt.imshow(image, cmap='gray')
        plt.axis('off')
        plt.show()

    def apply_morphological_operation(self):
        # original image
        plt.imshow(self.image, cmap='gray')
        plt.suptitle('original')
        plt.axis('off')
        plt.show()

        self.print_histogram(self.image)

        # thresholding
        mask_thresholding = self.image > 2

        plt.imshow(mask_thresholding, cmap='gray')
        plt.suptitle('thresholding')
        plt.axis('off')
        plt.show()

        # opening
        mask_opening = ndi.binary_opening(mask_thresholding, iterations=2)

        plt.imshow(mask_opening, cmap='gray')
        plt.suptitle('opening mask')
        plt.axis('off')
        plt.show()

        new_image = mask_opening * self.image

        plt.imshow(new_image, cmap='gray')
        plt.suptitle('new image after opening')
        plt.axis('off')
        plt.show()

    def print_histogram(self, image):
        hist = ndi.histogram(image, min=0,
                             max=255, bins=256)
        plt.plot(hist)
        plt.suptitle("Histogram")
        plt.show()

    def feature_detection(self):
        weights = [[+1, 0, -1], [+1, 0, -1], [+1, 0, -1]]

        mask = ndi.convolve(self.image, weights)

        plt.imshow(mask, cmap='gray')
        plt.suptitle('mask for feature detection')
        plt.axis('off')
        plt.show()

    def edge_detection(self):
        sobel_ax0 = ndi.sobel(self.image, axis=0)
        sobel_ax1 = ndi.sobel(self.image, axis=1)

        edges = np.sqrt(np.square(sobel_ax0) +
                        np.square(sobel_ax1))

        plt.imshow(edges, cmap='gray')
        plt.suptitle('mask for edge detection')
        plt.axis('off')
        plt.show()


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
