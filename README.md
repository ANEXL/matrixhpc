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
Median:       2.879805 s
Minimum:      2.812060 s
Mean:         2.901057 s
Std. dev.:    0.080647 s
Median:       0.75 GFLOP/s
Maximum:      0.76 GFLOP/s

Benchmarking cache_avoid_turns ...

cache_avoid_turns
----------------------------------------
Median:       0.398077 s
Minimum:      0.390901 s
Mean:         0.400001 s
Std. dev.:    0.009636 s
Median:       5.39 GFLOP/s
Maximum:      5.49 GFLOP/s

Benchmarking cache_avoid_transp ...

cache_avoid_transp
----------------------------------------
Median:       0.576965 s
Minimum:      0.565996 s
Mean:         0.585806 s
Std. dev.:    0.020581 s
Median:       3.72 GFLOP/s
Maximum:      3.79 GFLOP/s

Benchmarking cache_avoid_blocking ...

cache_avoid_blocking
----------------------------------------
Median:       0.465230 s
Minimum:      0.461117 s
Mean:         0.466171 s
Std. dev.:    0.004337 s
Median:       4.62 GFLOP/s
Maximum:      4.66 GFLOP/s

```
