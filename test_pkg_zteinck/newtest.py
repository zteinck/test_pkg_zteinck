from iterlab import to_iter
import pandas as pd
import numpy as np


def testaroo(x):
    # test
    if pd.isnull(x): return np.nan
    print(to_iter(x))