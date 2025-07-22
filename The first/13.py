import numpy as np
signal = np.array([0, 1, 0, 0])
fft_result = np.fft.fft(signal)
print(fft_result);