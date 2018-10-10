#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <malloc.h>
#include <sys/time.h>
#include <time.h>
#include <math.h>
#include <omp.h>

double my_timer() {
  struct timeval tv;
  struct timezone tz;
  gettimeofday(&tv, &tz);
  return ((double)tv.tv_sec + (double)0.000001 * (double)tv.tv_usec);
}

int main ( int argc, char * argv[] ) {

  omp_set_dynamic(0);
  int number_of_cores = atoi(argv[1]);
  omp_set_num_threads(number_of_cores);
  printf("Number of cores = %d\n", number_of_cores);

  uint64_t i, j, k;
  double * A = (double *) malloc(1000000 * sizeof(double *));
  double * B = (double *) malloc(1000000 * sizeof(double *));

  #pragma omp parallel for
  for (i = 0; i < 1000000; i ++) {
      A[i] = 1.0;
      B[i] = 1.0;
  }

  printf("C: Dot product 2 1000000 x 1000000 arrays (1 iteration)\n");
  double time1 = my_timer();

  double dot = 0.0;

  #pragma omp parallel for
  for (i = 0; i < 1000000; i ++) {
      dot += A[i] * B[i];
  }

  printf("dot product = %lf\n", dot);
}
