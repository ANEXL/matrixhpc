# matrixhpc
Collection of scripts in order to learn optimization in python and cpp at the example of matrix multiplication.
I want to improve in analysing code in terms of runtime, storage and ressource management and also develop skills in cpp and other HPC related languages such as CUDA, OpenMP, MPI und weitere.

## Results

### Naive

Benchmarked on 19.Aug.26
´´´
N:              1024
Seed:           42
Warmup Runs:    3
Benchmark Runs: 10
A gespeichert: data/A.bin
B gespeichert: data/B.bin

Benchmarking naive ...

naive
----------------------------------------
Median:       2.839265 s
Minimum:      2.798730 s
Mittelwert:   2.884498 s
Std. Abw.:    0.116598 s
Median:       0.76 GFLOP/s
Maximum:      0.77 GFLOP/s

´´´