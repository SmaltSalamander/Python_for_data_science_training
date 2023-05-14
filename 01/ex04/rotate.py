# %%
from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def main():
    racoon = ft_load("animal.jpeg")
    new_racoon = racoon[90:490, 450:850]
    print(new_racoon)
    rotated_racoon = np.array([new_racoon[:,number] for number in range(len(new_racoon) - 1, -1, -1)])
    rotated_racoon = Image.fromarray(rotated_racoon).convert('L')
    print(f"New shape after Transpose: {np.asarray(rotated_racoon).shape}")
    print(np.asarray(rotated_racoon))
    plt.imshow(rotated_racoon, cmap='gray')


if __name__ == "__main__":
    main()
# %%
