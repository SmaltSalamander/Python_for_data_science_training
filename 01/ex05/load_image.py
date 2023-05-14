from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """Loads an image and converts the result to an np array

    Args:
        path (str): path to the image

    Returns:
        np.array: image as an array
    """
    try: 
        img  = Image.open(path) 
    except IOError:
        return None
    img_np = np.asarray(img)
    print(f"The shape of image is: {img_np.shape}")
    return img_np

