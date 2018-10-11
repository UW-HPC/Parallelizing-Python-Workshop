# Lab Exercise 3

Please request a node and activate your environment before running the lab exercises. *Do not* run the lab exercises on the head node.

We encourage you to work on improving the sequential or parallel performance of your own code.  Instructors are available to help.  Before calling over an instructor, try to determine where you program spends most of its time or why it is not scaling.

If you don’t have a code to work on, here are two parallel programs you might try writing.  Both use the parallel programming concepts we discussed in lecture.

## Parallel PI

Picture the unit circle (radius = 1, centered on zero) inside the unit square.  The area of the circle divided by the area of the square is (&pi; r<sup>2</sup>) / (2 r)<sup>2</sup> = &pi; / 4.0.  A random (x, y) point, -1 < x < 1, -1 < y < 1, must fall within the square.  The probability that it also falls within the circle is proportional to the area of the circle.  Thus, if I generate X random points, the number of points that fall within the circle divided by the total number of points approaches &pi; / 4.0 as X approaches infinity. That is,

&pi; = 4.0 * (number of circle points / X)

Write a parallel Python program to calculate &pi;. Let X = 100,000.  Run the calculation 1000 times and average the values of &pi; computed.


## Breadth-First Search

Let G be a graph of vertices and directed edges.  Given a start vertex S, return all vertices reachable from S.  In your directory, the file edges gives a double column list of edges.  The first line is the number of vertices [0 .. N) and edges.  The rest of the lines give the source and destination vertex of an edge.

The most straightforward parallel implementation of BFS is the horizon method that keeps two lists: old and new.  Choose a start vertex, say vertex 0, and append it to old.  Now enter an iterative loop with the guard

	while len(old) != 0:

In the body of the loop, for each vertex v in old, examine the neighbors of v.  Append each unvisited neighbor to new.  At the bottom of the while loop, swap new and old. [How can you guarantee that you visit each vertex only once?]

To execute the algorithm, besides old and new, you will need two other data structures:

neighbors ¬– a list of integer lists.  The ith list holds the neighbors of vertex i.
visited ¬– an integer list.  The ith element is 0 if vertex i is unvisited; else 1.  Initialize the list to 0.

In your directory, open the file bfs.py.  I have started the code for you.  The file creates the processes, manager, and shared structures you will need to run the program.  Why do you need two locks?  Also, the file reads the edge file and creates the list of neighbors, edges.

