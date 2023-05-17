
import imageio.v2 as imageio
from sympy.codegen.fnodes import cmplx
import matplotlib.pyplot as plt


class Patient:
    vol = ''
    patient_info_keys = ['PatientName', 'PatientID', 'PatientBirthDate', 'PatientSex', 'PatientAge','SeriesNumber']
    image_info_keys = ['Modality','ImagePositionPatient', 'ImageOrientationPatient', 'SamplesPerPixel', 'Rows', 'Columns',
                       'PixelSpacing', 'HighBit', 'PixelRepresentation', 'RescaleIntercept', 'RescaleSlope', 'PixelData',
                       'shape', 'sampling']

    def __init__(self, dataset_path: object) -> object:
        # Load the "lung_CT CAP_data"" directory
        # D:\Faculty\4th year\2nd term\Biomedical Image Informatics\project\lab project\data\data\lung_data
        self.vol = imageio.volread(dataset_path, format='dicom')

    def patient_info(self):
        # print('Available metadata:', self.vol.meta())
        print('patient info')
        for key in self.patient_info_keys:
            print(key, ': ', self.vol.meta[key])

    def image_info(self):
        print('image info')
        for key in self.image_info_keys:
            print(key, ': ', self.vol.meta[key])

    def dataset_shape(self):
        # The shape of the stacked images in each plane
        # (Axial, Coronal, and Sagittal, respectively)
        n0, n1, n2 = self.vol.shape

        # Print the output
        print("Number of Slices:\n\t", "Axial=", n0,
              "Slices\n\t",
              "Coronal=", n1, "Slices\n\t",
              "Sagittal=", n2, "Slices")
        return [n0, n1, n2]

    def dataset_sampling(self):
        # The sampling of the dataset images in each plane
        # (Axial, Coronal, and Sagittal, respectively)
        d0, d1, d2 = self.vol.meta['sampling']

        # Print the output
        print("Sampling:\n\t", "Axial=", d0, "mm\n\t",
              "Coronal=", d1, "mm\n\t",
              "Sagittal=", d2, "mm")

        return [d0, d1, d2]

    def dataset_aspect_raito(self, d):
        axial_asp = d[1] / d[2]
        # The aspect ratio along the sagittal plane
        sagittal_asp = d[0] / d[1]
        # The aspect ratio along the coronal plane
        coronal_asp = d[0] / d[2]
        # Print the output

        print("Pixel Aspect Ratio:\n\t", "Axial=", axial_asp, "\n\t",
              "Coronal=", coronal_asp, "\n\t", "Sagittal=", sagittal_asp)

    def dataset_feild_Of_View(self, d, n):
        print("Field of View:\n\t", "Axial=", n[0] * d[0],
              "mm\n\t", "Coronal=", n[1] * d[1], "mm\n\t",
              "Sagittal=", n[2] * d[2], "mm")

    def dataset_info(self):
        # images shape
        n = self.dataset_shape()

        # print dataset sampling
        d = self.dataset_sampling()

        # print dataset aspect ratio
        self.dataset_aspect_raito(d)

        # print field of view of dataset image
        self.dataset_feild_Of_View(d, n)

        return d

    def show_patient_image(self, d):
        # axial image
        im1 = self.vol[70, :, :]

        # coronal image
        im2 = self.vol[:, 300, :]

        # sagittal image
        im3 = self.vol[:, :, 300]

        # Compute aspect ratios
        asp1 = d[0] / d[2]
        asp2 = d[0] / d[1]

        # Initialize figure and axes grid
        fig, axes = plt.subplots(nrows=1, ncols=3)
        # Draw an images for 3 planes on each subplot
        axes[0].imshow(im1, cmap='gray')
        axes[1].imshow(im2, cmap='gray', aspect=asp1)
        axes[2].imshow(im3, cmap='gray', aspect=asp2)

        # Remove ticks/labels and render
        axes[0].axis('off')
        axes[1].axis('off')
        axes[2].axis('off')
        plt.show()

    def print_info(self):
        # print patient information.
        self.patient_info()
        # print Image information.
        self.image_info()

        # print Shape, Sampling, Pixel Aspect ratio and field of view of the images used.
        d = self.dataset_info()

        # show Slice the image to view from different planes
        self.show_patient_image(d)


# def _main_():
#     path = '3.000000-Lung 3.0-46505'
#    # path = '..\\data\\data\\lung_CT CAP_data'
#     patient = Patient(path)
#     patient.print_info()


# _main_()
