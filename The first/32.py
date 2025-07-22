import numpy as np
from scipy.integrate import quad
result, error = quad(lambda x: x**2, 0, 1)
print(result);