

1. Profile simul.py

  ```
  $ python -m cProfile simul.py
  $ python -m cProfile -s tottime simul.py
  $ python -m cProfile -o prof.out simul.py
  ```

2. You can also use cProfile within your code to profile just certain pieces:

  ```Python
  from simul import benchmark
  import cProfile

  pr = cProfile.Profile()
  pr.enable()
  benchmark()
  pr.disable()
  pr.print_stats()
  ```

  Pick one of the programs you wrote in previous labs.  What are the hotspots?  If you have program of your own, run the profiler on it.

  Experiment with increasing the number of particles.

3. There is a small program in the lab directory named factorial.py.  Take its profile and inspect with qcachegrind.  As before, experiment with some of the programs you have written before.

4. Use line_profiler to explore (e.g., with kernprof) to investigate simul, factorial, and some of your own programs.
