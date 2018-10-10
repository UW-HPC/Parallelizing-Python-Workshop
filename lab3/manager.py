import os
import sys
import time
from collections import defaultdict
from multiprocessing import Process, Lock, Manager

processes = [ ]

file = open('article', mode = 'r')
lines = file.read().split('.')
file.close()

manager = Manager()
bag = manager.dict()
lock = manager.Lock()
delims = manager.list([',', ';', ':', '-', '.'])

def bag_of_words(line, l, d, delims):
  my_dict = defaultdict(int)

  for d in delims:
    line = line.replace(d, ' ')

  for word in line.split():
    my_dict[word] += 1

  lock.acquire()

  for key, value in my_dict.iteritems():
    try:
      bag[key] += value
    except KeyError:
      bag[key] = value

  lock.release()

time1 = time.time()

for line in lines:
    p = Process(target=bag_of_words, args=(line, lock, bag, delims,))
    processes.append(p)
    p.start()

for p in processes:
  p.join()

time2 = time.time() - time1
print bag
print("Time = {0}".format(time2))
