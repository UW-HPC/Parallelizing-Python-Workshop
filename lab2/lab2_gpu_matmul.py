import os
import sys
import time
import numba
import numpy
from numba import prange
from numba import cuda

# from numba import float32, float64




@cuda.jit
def matmul_gpu(C, A, B):
    i, j = cuda.grid(2)
    if i < C.shape[0] and j < C.shape[1]:
        # your inner loop goes here (hint: think dot product)


@numba.jit(['void(float64[:,:],float64[:,:],float64[:,:])','void(float32[:,:],float32[:,:],float32[:,:])' ] , nopython=True, parallel=True)
def matmul_cpu(C, A, B):
    # your python matmul goes here


def main():
    
    N = 64
    dtype = 'float32'

    if len(sys.argv) >= 2:
        N = int(sys.argv[1])
    if len(sys.argv) >= 3:
        if sys.argv[2] == "double":
            dtype = 'float64'

    A = numpy.ones([N, N], dtype=dtype);
    B = numpy.ones([N, N], dtype=dtype);
    C = numpy.zeros([N, N], dtype=dtype);

    time1 = time.time()
    matmul_cpu(C, A, B)
    time2 = time.time() - time1
    print("Time to multiply 2 %d x %d arrays in Python = {0}".format(time2) % (N, N))
    print("check: %g %g" % (C[0,0],C[N-1,N-1]))

    C = numpy.zeros([N, N], dtype=dtype);

    time1 = time.time()
    matmul_gpu(C, A, B)
    time2 = time.time() - time1
    print("GPU ime to multiply 2 %d x %d arrays in Python = {0}".format(time2) % (N, N))
    print("check: %g %g" % (C[0,0],C[N-1,N-1]))



