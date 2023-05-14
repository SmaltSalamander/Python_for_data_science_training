# %%
from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def ft_invert(array) -> np.array:
    inverted_img = 255 - array
    return inverted_img

def ft_red(array) -> np.array:
    red_image = np.array(array)
    red_image[...,1] = 0
    red_image[...,2] = 0
    return red_image

def ft_green(array) -> np.array:
    green_image = np.array(array)
    green_image[...,0] = 0
    green_image[...,2] = 0
    return green_image

def ft_blue(array) -> np.array:
    blue_image = np.array(array)
    blue_image[...,0] = 0
    blue_image[...,1] = 0
    return blue_image

def ft_grey(array) -> np.array:
    max_rgb = np.amax(array)
    gray_img = np.array([[max(array[i,j,:]) / max_rgb 
                         for j in range(array.shape[1])]
                         for i in range(array.shape[0])])
    return gray_img


def main():
    landscape = ft_load("landscape.jpg")
    ft_grey(landscape)
    # plt.imshow(ft_grey(landscape), cmap='gray')
    plt.imshow(ft_invert(landscape))

if __name__ == "__main__":
    main()
# %%
