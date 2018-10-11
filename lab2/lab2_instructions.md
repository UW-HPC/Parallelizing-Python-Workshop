# Lab Exercises 2

Please request a node and activate your environment before running the lab exercises. *Do not* run the lab exercises on the head node.

1. Repeat Lab 1 exercise (use your previous slow python code.
Put the code into a separate function and annotate it with @numba.jit.

How does the time compare to numpy?

You can get more documentation about the numba jit with

print(numba.jit.__doc__)

Full documentation is here:

https://numba.pydata.org/numba-doc/dev/user/index.html

2. To get parallelism with @numba.jit you should specify parallel ranges for your indices.  To use parallel ranges:

from numba import prange

and use it as follows

for i in prange(A.shape[0]):

First try using just one prange in different loops.  Next try multiple loops at the same time.  With which do you get best performance?  How much speedup do you get versus the number of processors that you have?

3. There is an example program in lab2/lab2-axpy.py.  This program uses numba.cuda.jit.  It takes as a command-line argument the size of the matrix to be multiplied, the number of "trials" to run with the kernel, and the type of data to use.  

Try the following runs:

python lab2-axpy.py 100 1 
python lab2-axpy.py 10000 1 
python lab2-axpy.py 1000000 1
python lab2-axpy.py 2000000 1
python lab2-axpy.py 2000000 1 double
python lab2-axpy.py 20000000 1 
python lab2-axpy.py 20000000 1 double

Do these results make sense?

Right now the variable "trips" isn't used. Try putting it in the outer loop and the inner loop.  Is there a difference in performance?

Repeat the above experiments but add a large number of lops.  Note that the "trips" printed out by the program should match your number of trips provided on the command line.

Finally, add the following import to the file

from numba import float32, float64

What happens?

4. Because cuda is often (mostly?) used for scientific computation, it provides a different means of accessing thread indices.  In particular, you can put the threads into a 2D grid.

You can get the i and j values for the arrays (let's assume they are all the same dimension for now) this way:

(i, j) = cuda.grid(2)

You can use these as indices into your matrices and elide two loops:  Each inner loops is done in a different thread.

Implement a gpu matmul kernel using this idea. Skeleton code is in lab2_gpu_matmul.py

Hint: For an N by N matrix where we are going to assign one thread to each matrix element, how many threads to we need to specify at launch?  How might we break that into blocks and threads?

Note that the code makes sure the thread indices are valid.

5. We haven't tested the matmul yet.

Add the following lines after the existing print

    print("check: %g %g" % (C[0,0],C[N-1,N-1]))

Does everything work?  What is wrong with our assumptions about the gpu grid?

As we saw with axpy, we need to specify the number of threads to use.  In this case, we now need to specify them in a 2D grid.  Modify the kernel launch to use a 2D grid.

6. At what size does the GPU version have better performance than CPU?




