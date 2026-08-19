# matrixhpc
Collection of scripts in order to learn optimization in python and cpp at the example of matrix multiplication.
I want to improve in analysing code in terms of runtime, storage and ressource management and also develop skills in cpp and other HPC related languages such as CUDA, OpenMP, MPI und weitere.

## Results

Benchmarked on 19.Aug.26
```
============================================================
Matrix Multiplication Benchmark
============================================================
N:              1024
Seed:           42
Warmup Runs:    3
Benchmark Runs: 10
A gespeichert: data/A.bin
B gespeichert: data/B.bin

Benchmarking naive ...

naive
----------------------------------------
Median:       2.814415 s
Minimum:      2.763590 s
Mittelwert:   2.810138 s
Std. Abw.:    0.034149 s
Median:       0.76 GFLOP/s
Maximum:      0.78 GFLOP/s
Benchmarking cache_avoid ...

cache_avoid
----------------------------------------
Median:       0.394751 s
Minimum:      0.389528 s
Mittelwert:   0.395320 s
Std. Abw.:    0.004778 s
Median:       5.44 GFLOP/s
Maximum:      5.51 GFLOP/s
```
