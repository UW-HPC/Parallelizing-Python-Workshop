import sys
import numpy
import datetime

import numba
from numba import cuda, float32, float64

@cuda.jit
def axpy(a, x, y, trips):
    tx = cuda.threadIdx.x
    ty = cuda.blockIdx.x
    bw = cuda.blockDim.x
    pos = tx + ty * bw

    if pos < x.size:
        for i in (range(trips)):
            y[pos] = y[pos] + a*x[pos]

def main():
    
    N = 1024 * 128;
    trips = 1
    dtype = 'float32'
    
    if len(sys.argv) >= 2:
        N = int(sys.argv[1])
    if len(sys.argv) >= 3:
        trips = int(sys.argv[2])
    if len(sys.argv) >= 4:
        if sys.argv[2] == "double":
            dtype = 'float64'
            
    alpha = 1.000000001;
    x = numpy.ones(N, dtype=dtype)
    y = numpy.ones(N, dtype=dtype)

    y[0] = 0;  y[N-1] = 0;
    start = datetime.datetime.now()
    axpy[(N+255)//256, 256](alpha, x, y, trips)
    stop = datetime.datetime.now()
    print ('Elapsed time : %s, trips = %g, %g' % (str( stop - start ), y[0], y[N-1]))

main()
