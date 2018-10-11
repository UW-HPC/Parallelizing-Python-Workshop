# Lab Exercises 1

Please request a node and activate your environment before running the lab exercises. *Do not* run the lab exercises on the head node.

1. Numpy is an optimized numeric Python package.  It stores multi-dimensional, numeric structures in continuous memory and makes use of vector instructions.  Consequently, Numpy statements execute many orders of magnitude faster than equivalent Python statements.

Open the script matmul.py and replace the ellipses (lines 7, 8, 9,  22, 23, 24, and 25) with Python code.

We will use Python’s time.time method to time our code.  Now run the python script, “python matmul.py”.  The script will take many minutes to run as Python is SLOW.  Kill the script after a minute or so.

2. Now open the script matmul.np.py, and replace the ellipses (lines 8, 9, 10, and 15) with Numpy statements.  Google or ask the instructors for help.  Run the script.  Notice how much faster the Numpy code is.  You want to use Numpy whenever possible.

3. By storing values in continuous memory, Numpy reduces cache misses as we discussed in the lecture.  When a value is read from memory, the processor transfers a cache line (usually 8 words) to the L1 cache.  When values are accessed in continuous order, the first word will cause a miss cache, but the next seven words will be read from cache.

Open the script cacheEffects.1.py.  The script computes the dot product of two vectors.  Close the script and run it.  Note the time.

Now open the script cacheEffects.all.py.  Replace the ellipsis with Numpy code to compute the dot product of A and B skipping elements.  Google or ask the instructors for help.  Close the script and run it.  Why is the time similar for the first four runs and decrease for the last two?

4. We are now going to switch to C.  It is okay if you don’t know C.  It is easier to demonstrate parallel computing concepts in C code than Python code.  Open the file matmul.cc.  Find the main program starting on line 16.  Look at lines 19 and 20.  These two statements set the number of cores that the program will use.  Notice the `#pragma omp` statements (line 28, 35, and 46).  These statements instruct the compiler to parallelize the for loop that follows.  Now close the file and compile it.  Ask the instructor for the compile command.

Run the program giving the number of cores to use as a command line parameter.  Ask the instructors for help.  Run the program for 1, 2, 4, and 8 cores.  Note the reduction in execution time as you use more cores.

5. For the final exercise, open the file dotproduct.cc.  The parallel for loop on line 38 computes the dot product of A and B.  Close the file, compile it, and run it for different numbers of cores.  Why are you getting different results?  What’s wrong with the parallel for loop?

Refer back to the lecture and fix the for loop (there are three ways to fix the loop).  Ask the instructors for help.  If you can, implement all three fixes.  Which fixes are fastest?  Why?

