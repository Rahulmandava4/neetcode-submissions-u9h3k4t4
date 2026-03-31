import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        sigmoidfunc = lambda x : (1/(1 + (math.e)**(-x)))
        vectorizefunc = np.vectorize(sigmoidfunc)
        result = vectorizefunc(z)
        return np.round(result,5)

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        relufunc = lambda x : x if x>0 else 0
        vectorizefunc = np.vectorize(relufunc,otypes = [float])
        result = vectorizefunc(z)
        return np.round(result,5)
