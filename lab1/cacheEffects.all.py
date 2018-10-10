import os
import sys
import time
import numpy

a = numpy.full(20000000, 1.0, dtype = numpy.float64)
b = numpy.full(20000000, 1.0, dtype = numpy.float64)

# Stride 1
time1 = time.time()
for _ in range(2000):
  sum = numpy.dot(a, b)

time2 = time.time() - time1
print("Time for dot product of 20M elements, stride  1, 40.0M FLOPS, (2000 iterations) = {0}".format(time2))


# Stride 2
time1 = time.time()
for _ in range(2000):
  sum = ...

time2 = time.time() - time1
print("Time for dot product of 20M elements, stride  2, 20.0M FLOPS, (2000 iterations) = {0}".format(time2))


# Stride 4
time1 = time.time()
for _ in range(2000):
  sum = ...

time2 = time.time() - time1
print("Time for dot product of 20M elements, stride  4, 10.0M FLOPS, (2000 iterations) = {0}".format(time2))


# Stride 8
time1 = time.time()
for _ in range(2000):
  sum = ...

time2 = time.time() - time1
print("Time for dot product of 20M elements, stride  8,  5.0M FLOPS, (2000 iterations) = {0}".format(time2))


# Stride 16
time1 = time.time()
for _ in range(2000):
  sum = ...

time2 = time.time() - time1
print("Time for dot product of 20M elements, stride 16,  2.5M FLOPS, (2000 iterations) = {0}".format(time2))


# Stride 32
time1 = time.time()
for _ in range(2000):
  sum = ...

time2 = time.time() - time1
print("Time for dot product of 20M elements, stride 32,  1.25M FLOPS, (2000 iterations) = {0}".format(time2))
