import os
import sys
import time
import numpy
import multiprocessing
from multiprocessing import Queue

size = 2000000
number_processes = 4
chuck_size = size / number_processes

a = numpy.full(size, 1.0, dtype = numpy.float64)
b = numpy.full(size, 1.0, dtype = numpy.float64)

q = Queue()
processes = [ ]

def dotproduct_mp(a, b):
  c = numpy.dot(a, b)
  q.put(c)

time1 = time.time()

for i in range(number_processes):
    lb = i * chuck_size
    ub = lb + chuck_size
    p = multiprocessing.Process(target=dotproduct_mp, args=(a[lb:ub], b[lb:ub],))
    processes.append(p)
    p.start()

for p in processes:
  p.join()


dot = 0.0
while not q.empty():
  dot += q.get()

time2 = time.time() - time1
print("dot product = ", dot)
print("Time = {0}".format(time2))
