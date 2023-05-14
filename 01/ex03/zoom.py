# %%
from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def main():
    racoon = ft_load("animal.jpeg")
    print(racoon)
    new_racoon = racoon[90:490, 450:850]
    new_racoon = Image.fromarray(new_racoon).convert('L')
    print(f"New shape after slicing: {np.asarray(new_racoon).shape}")
    plt.imshow(new_racoon, cmap='gray')
    print(new_racoon)



if __name__ == "__main__":
    main()
# %%
