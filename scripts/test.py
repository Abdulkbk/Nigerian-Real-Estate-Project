import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

data = pd.read_csv('../data/nigerian_real_estate.csv')

mapper = {
    "1": int(1),
    "2": 2,
    "3": 3,
    "4": 4,
    "5": int(5),
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "None": np.nan
}
print(data['bedrooms'].map(mapper))

print(data['bedrooms'])