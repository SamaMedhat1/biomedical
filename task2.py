import imageio.v2 as imageio
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as ndi


# segment object of interest
def object_segmentation(image_path):
    im = imageio.imread(image_path)
    im_filt = ndi.median_filter(im, size=3)
    mask_start = np.where(im_filt > 60, 1, 0)
    mask = ndi.binary_closing(mask_start)
    labels, nlabels = ndi.label(mask)
    print('Num. Labels:', nlabels)
    overlay = np.where(labels > 0, labels,
                       np.nan)
    fig, axes = plt.subplots(nrows=1, ncols=2)
    axes[0].imshow(im, cmap='gray')
    axes[1].imshow(overlay, cmap='rainbow')

    axes[0].axis('off')
    axes[1].axis('off')

    plt.show()

object_segmentation("CT_data/000055.dcm")