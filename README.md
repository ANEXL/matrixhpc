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
Median:       2.802030 s
Minimum:      2.749730 s
Mittelwert:   2.810772 s
Std. Abw.:    0.055323 s
Median:       0.77 GFLOP/s
Maximum:      0.78 GFLOP/s

Benchmarking cache_avoid_turns ...

cache_avoid_turns
----------------------------------------
Median:       0.404657 s
Minimum:      0.388602 s
Mittelwert:   0.410847 s
Std. Abw.:    0.023941 s
Median:       5.31 GFLOP/s
Maximum:      5.53 GFLOP/s

Benchmarking cache_avoid_transp ...

cache_avoid_transp
----------------------------------------
Median:       0.566099 s
Minimum:      0.560622 s
Mittelwert:   0.566845 s
Std. Abw.:    0.003509 s
Median:       3.79 GFLOP/s
Maximum:      3.83 GFLOP/s
```
