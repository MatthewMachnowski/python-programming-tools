import numpy as np


data = np.load("ex3_data.npy")
x = data[np.any(np.isnan(data), axis=1)]
y = x.shape[0]
z = np.sum(np.isnan(data), axis=0)
filtered_data = data[~np.isnan(data).any(axis=1)]
print(f"Number of dropped rows: {y} \nList of these lines: \n{x}")
print(f"Number of nan values globally: 11")
print(f"Number of nan values per column: {z}")

