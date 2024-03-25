import numpy as np
from scipy.fft import fft
def DFT_slow(x):
    x = np.asarray(x, dtype=float)# ensure the data type
    N = x.shape[0]                # get the x array length
    n = np.arange(N)              # 1d array
    k = n.reshape((N, 1))       # 2d array, 10 x 1, aka column array
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)       # [a,b] . [c,d] = ac + bd, it is a sum
x = np.random.random(1024)
np.allclose(DFT_slow(x), fft(x))