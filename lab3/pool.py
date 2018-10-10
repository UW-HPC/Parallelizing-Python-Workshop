import os
import sys
import time
import numpy
import multiprocessing
from functools import partial
from multiprocessing import Pool

size = 2000000
number_cores = 4
a = numpy.full(size, 1.0, dtype = numpy.float64)
b = numpy.full(size, 1.0, dtype = numpy.float64)

def vector_square(x):
  return x * x

def vector_add(elem_list):
  return sum(elem_list)

def elem_elem_add(a, b, i):
  return a[i] + b[i]

def THICK_elem_elem_add(a, b, number_cores, i):
  slice_size = a.size / number_cores
  lb = slice_size * i;
  ub = lb + slice_size;
  return a[lb:ub] + b[lb:ub]

time1 = time.time()

pool = Pool(number_cores)
c = pool.map(vector_square, a)
pool.close()
pool.join()

time2 = time.time() - time1
print("Time for vector_square \t\t = {0}".format(time2))


time1 = time.time()

pool = Pool(number_cores)
c = pool.map(vector_add, zip(a, b))
pool.close()
pool.join()

time2 = time.time() - time1
print("Time for vector_add \t\t = {0}".format(time2))


time1 = time.time()

pool = Pool(number_cores)
map_func = partial(elem_elem_add, a, b)
c = pool.map(map_func, iter(range(size)))
pool.close()
pool.join()

time2 = time.time() - time1
print("Time for elem_elem_add \t\t = {0}".format(time2))


time1 = time.time()

pool = Pool(number_cores)
map_func = partial(THICK_elem_elem_add, a, b, number_cores)
c = pool.map(map_func, iter(range(number_cores)))
pool.close()
pool.join()

time2 = time.time() - time1
print("Time for THICK_elem_elem_add \t = {0}".format(time2))
