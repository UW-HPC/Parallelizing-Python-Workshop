#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
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
  double ** A = (double **) malloc(1500 * sizeof(double *));
  double ** B = (double **) malloc(1500 * sizeof(double *));
  double ** C = (double **) malloc(1500 * sizeof(double *));

  #pragma omp parallel for
  for (i = 0; i < 1500; i ++) {
      A[i] = (double *) malloc(1500 * sizeof(double));
      B[i] = (double *) malloc(1500 * sizeof(double));
      C[i] = (double *) malloc(1500 * sizeof(double));
  }

  #pragma omp parallel for
  for (i = 0; i < 1500; i ++) {
  for (j = 0; j < 1500; j ++) {
      A[i][j] = 1.0;
      B[i][j] = 1.0;
      C[i][j] = 0.0;
  } }

  printf("C: Matrix multiply 2 1500 x 1500 arrays (1 iteration)\n");
  double time1 = my_timer();

  #pragma omp parallel for
  for (i = 0; i < 1500; i ++) {
  for (j = 0; j < 1500; j ++) {
  for (k = 0; k < 1500; k ++) {
      C[i][j] += A[i][k] * B[k][j];
  } } }

  printf("%lf\n", my_timer() - time1);
}
