from tkinter import *

import classification
from Patient import *
from ImageAnalysis import *
from classification import *
import cv2 as cv
import skimage

# for using function here !
Gui = Tk()

# the title of GUI window
Gui.title("Biomedical Project")

# the configuration of GUI window
Gui.geometry("450x400")

# path of data set
path = 'archive'


# action button 1 (Task 1)
def CheckBtn1():
    patient_all_ = Patient(path)
    patient_all_.print_info()


# action button 2 (Task 2)
def CheckBtn2():
    image_analysis = ImageAnalysis()

    # point one / task 2
    image_analysis.apply_morphological_operation()

    # point two/ task 2
    image_analysis.feature_detection()
    image_analysis.edge_detection()

    # point three and four / task 2
    labels = image_analysis.segment_objects()
    image_analysis.extract_cancer(labels)
    image_analysis.calc_area(labels)
    image_analysis.distance_transformation(labels)
    image_analysis.center_mass(labels)


def CheckBtn3():
    classifier = Classification()
    path1 = cv2.imread('Cofield.45.jpg', 0)
    classifier.print_c(path1)

    path2 = cv2.imread('Cofield.70.jpg', 0)
    classifier.print_c(path2)

    path3 = cv2.imread('Depuy.236.jpg', 0)
    classifier.print_c(path3)
    path4 = cv2.imread('Depuy.250.jpg', 0)
    classifier.print_c(path4)

    path5 = cv2.imread('Tornier.65.jpg', 0)
    classifier.print_c(path5)
    path6 = cv2.imread('Tornier.67.jpg', 0)
    classifier.print_c(path6)

    path7 = cv2.imread('Zimmer.135.jpg', 0)
    classifier.print_c(path7)
    path8 = cv2.imread('Zimmer.148.jpg', 0)
    classifier.print_c(path8)


# button for Task 1
btn = Button(Gui, text='Task 1', command=CheckBtn1, width=20)
btn.place(x=150, y=50)

# button for Task 2
btn2 = Button(Gui, text='Task 2', command=CheckBtn2, width=20)
btn2.place(x=150, y=150)

# button for Task 3
btn3 = Button(Gui, text='Task 3', command=CheckBtn3, width=20)
btn3.place(x=150, y=250)

# start the GUI
Gui.mainloop()
