import numpy as np

data = np.array([10, 20, 30, 40, 50])
data_range = np.max(data) - np.min(data)

print(f"Range: {data_range}")