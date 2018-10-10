import os
import sys
import time

# Define three 1500 x 1500 python double precision matrices, A, B, and C.
# Fill A and B with some double value; fill C with 0.0
A = ...
B = ...
C = ...

print
print "PYTHON: Matrix multiply 2 1500 x 1500 arrays (1 iteration)"
print "******                                                         ******"
print "******                                                         ******"
print "****** WHEN YOU GET TIRED OF WAITING, KILL THE PROGRAM (Ctl-C) ******"
print "******                                                         ******"
print "******                                                         ******"

time1 = time.time()

# Write a for loop (i, j, k) to compute C = A * B
for i in ...
    for j in ...
        for k in ...
            ...

time2 = time.time() - time1
print("Time to multiply 2 1500 x 1500 arrays in Python = {0}".format(time2))
