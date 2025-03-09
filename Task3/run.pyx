import numpy as np
cimport numpy as np

def calculateEnergyConsumption(np.ndarray[np.float64_t, ndim=2] powerMatrix, np.ndarray[np.float64_t, ndim=2] timeMatrix):

    
    cdef int nrows = powerMatrix.shape[0]
    cdef int ncols = powerMatrix.shape[1]
    cdef np.ndarray[np.float64_t, ndim=2] result = np.empty((nrows, ncols), dtype=np.float64)
    
    for i in range(nrows):
        for j in range(ncols):
            result[i, j] = powerMatrix[i, j] * timeMatrix[i, j]
    
    return result
