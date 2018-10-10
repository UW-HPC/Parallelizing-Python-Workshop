import os
import sys
import time
from multiprocessing import Process, Manager

file = open('edges', mode = 'r')
lines = file.readlines()
file.close()

num_vertices = int( (lines[0].split())[0] )
num_edges = int( (lines[0].split())[1] )
print("Number of vertices = {0}, Number of edges = {1}".format(num_vertices, num_edges))

# Declare shared lists
processes = [ ]
manager = Manager()

old = manager.list()
new = manager.list()
edges = manager.list()
visited = manager.list([0] * num_vertices)

lock_new = manager.Lock()
lock_visited = manager.Lock()

# Initialize neighbor list
edge_list = [ ]
src = int( (lines[1].split())[0] )
dst = int( (lines[1].split())[1] )

# Neighbor lists for vertices 0 to first src are empty
for i in range(src):
  edges.append(edge_list)

for line in lines[2:]:
  edge_list.append(dst)
  next_src = int( (line.split())[0] )
  next_dst = int( (line.split())[1] )

  if next_src != src:
     edges.append(edge_list)

     # Append neighbor list for src; then neighbor lists for vertices src to next src are empty
     for _ in range(src + 1, next_src):
       edge_list = [ ]
       edges.append(edge_list)

     edge_list = [ ]

  src = next_src
  dst = next_dst

# Append neighbor list for last src
edges.append(edge_list)

# Neighbor lists for last src to number of vertices are empty
edge_list = [ ]
for _ in range(src + 1, num_vertices):
   edges.append(edge_list)


# BFS function
# ... write bfs function here
# ...

# *****  BEGIN BFS *****
print "Starting BFS"
time1 = time.time()

# Start at vertex 0
old.append(0)

while len(old) != 0:

# ... write master code here
# ...
# ...

# Swap old and new lists
  old = new
  new = manager.list()

  print len(old)

time2 = time.time() - time1
print("BFS time = {0}".format(time2))
