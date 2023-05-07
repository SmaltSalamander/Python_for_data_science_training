import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    print(f"My shape is : {np.asarray(family).shape}")
    result = family[start:end]
    print(f"My shape is : {np.asarray(result).shape}")
    return result

