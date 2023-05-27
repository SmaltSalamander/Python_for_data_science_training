import pandas as pd
import numpy as np
import os

def load(path: str) -> pd.DataFrame:
    """Loads a csv file after ascertaining the file's existence and type

    Args:
        path (str): Path to the csv file

    Returns:
        pd.DataFrame: the dataset in a DataFrame format
    """
    try:
        assert os.path.exists(path)
        pd_arr = pd.read_csv(path)
        print(f"Loading dataset of dimensions: {pd_arr.shape}")
        return pd_arr
    except AssertionError as exc:
        print(f"{type(exc).__name__}: Path couldn't be accessed/doesn't exist")
    except pd.errors.ParserError as exc:
        print(f"{type(exc).__name__}: Bad format")
    return None
