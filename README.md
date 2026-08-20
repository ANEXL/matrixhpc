# matrixhpc
Collection of scripts in order to learn optimization in python and cpp at the example of matrix multiplication.
I want to improve in analysing code in terms of runtime, storage and ressource management while also develop skills in cpp as well as other HPC related languages such as CUDA, OpenMP and MPI.

## Benchmarking
The benchmark script creates two matrices with a given Problemsize N², outputs them as binarys to the ./data folder and runs all linkes executables with a given number of warm-up and measurment runs.
The output is the calculation time (med,min,max,std.dev,...) and the GFLOPS/s calculated with the following formula:
$\frac{2 \cdot N^{3}}{t_{med|max} \cdot 10^{9}}$

## Results

Benchmarked on 20.Aug.26
```
============================================================
Matrix Multiplication Benchmark
============================================================
N:              1024
Seed:           42
Warmup Runs:    3
Benchmark Runs: 10
A saved: data/A.bin
B saved: data/B.bin


Benchmarking naive ...

naive
----------------------------------------
Median:       2.785080 s
Minimum:      2.764790 s
Mittelwert:   2.801623 s
Std. Abw.:    0.033812 s
Median:       0.77 GFLOP/s
Maximum:      0.78 GFLOP/s

Benchmarking cache_avoid_turns ...

cache_avoid_turns
----------------------------------------
Median:       0.447667 s
Minimum:      0.387280 s
Mittelwert:   0.426507 s
Std. Abw.:    0.031894 s
Median:       4.80 GFLOP/s
Maximum:      5.55 GFLOP/s

Benchmarking cache_avoid_transp ...

cache_avoid_transp
----------------------------------------
Median:       0.561809 s
Minimum:      0.559867 s
Mittelwert:   0.565054 s
Std. Abw.:    0.006213 s
Median:       3.82 GFLOP/s
Maximum:      3.84 GFLOP/s
```
