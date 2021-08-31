"""
Defines things related to posterization of image.

Posterization of an image entails the conversion of a continuous gradation of tone to several
regions of fewer tones. -- from Wikipedia
"""

import sys

import matplotlib.pyplot as plt
import numpy as np
import cv2

# from '1 GRASS' to '61 GLOW_LICHEN' according to the wikipedia page
# https://minecraft.fandom.com/wiki/Map_item_format#Color_table
USABLE_COLORS = [[127, 178, 56], [247, 233, 163], [199, 199, 199], [255, 0, 0], [160, 160, 255],
                 [167, 167, 167], [0, 124, 0], [255, 255, 255], [164, 168, 184], [151, 109, 77],
                 [112, 112, 112], [64, 64, 255], [143, 119, 72], [255, 252, 245], [216, 127, 51],
                 [178, 76, 216], [102, 153, 216], [229, 229, 51], [127, 204, 25], [242, 127, 165],
                 [76, 76, 76], [153, 153, 153], [76, 127, 153], [127, 63, 178], [51, 76, 178],
                 [102, 76, 51], [102, 127, 51], [153, 51, 51], [25, 25, 25], [250, 238, 77],
                 [92, 219, 213], [74, 128, 255], [0, 217, 58], [129, 86, 49], [112, 2, 0],
                 [209, 177, 161], [159, 82, 36], [149, 87, 108], [112, 108, 138], [186, 133, 36],
                 [103, 117, 53], [160, 77, 78], [57, 41, 35], [135, 107, 98], [87, 92, 92],
                 [122, 73, 88], [76, 62, 92], [76, 50, 35], [76, 82, 42], [142, 60, 46],
                 [37, 22, 16], [189, 48, 49], [148, 63, 97], [92, 25, 29], [22, 126, 134],
                 [58, 142, 140], [86, 44, 62], [20, 180, 133], [100, 100, 100], [216, 175, 147],
                 [127, 167, 150]]


def simple_lab_euclid(image_rgb, colors_rgb):
    """
    Weight-less and element-wise posterization in CIELAB color space with Euclid distancing.

    Args:
        image_rgb (np.ndarray): Input image in RGB space and np.uint8 type.
        colors_rgb (np.ndarray): A set of target colors in RGB space and np.uint8 type.

    Returns:
        np.ndarray: an array of indices of the input color array
    """
    image_lab = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2LAB)
    # cv2.cvtColor only accepts 2D images
    # so use np.newaxis to reshape the color list from Nx3 to 1xNx3, and then restore the old shape
    colors_lab = cv2.cvtColor(colors_rgb[np.newaxis], cv2.COLOR_RGB2LAB).reshape(-1, 3)
    # use np.newaxis to cater the broadcasting rules of numpy
    # https://numpy.org/doc/stable/user/basics.broadcasting.html
    dist = ((image_lab[:, :, np.newaxis, :].astype(int) - colors_lab) ** 2).sum(axis=3)
    return np.argmin(dist, axis=2)


def main():
    """
    Entrypoint of posterization.py, mainly used as a simple showcase.
    """
    import logging

    logging.basicConfig(level='INFO')
    # logging.basicConfig(level='DEBUG')

    logging.info(img_path := sys.argv[1])
    image_rgb = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB)
    colors_rgb = np.array(USABLE_COLORS).astype(np.uint8)
    result_rgb = colors_rgb[simple_lab_euclid(image_rgb, colors_rgb)]

    fig, axs = plt.subplots(1, 2)
    axs[0].imshow(image_rgb)
    axs[1].imshow(result_rgb)
    axs[0].set_title('original', fontweight='bold')
    axs[1].set_title('simple LAB Euclid', fontweight='bold')
    fig.show()


if __name__ == '__main__':
    main()
