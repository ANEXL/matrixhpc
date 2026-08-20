import subprocess
import numpy as np
import os

#  Benchmark settings
N = 1024 # Problem size (matrix dimension)
SEED = 42

RUNS = 10
WARMUP_RUNS = 3

DATA_DIR = "data"

A_FILE = f"{DATA_DIR}/A.bin"
B_FILE = f"{DATA_DIR}/B.bin"

IMPLEMENTATIONS = {
    "naive": ["./naive/matrixhpcdummy"],
    "cache_avoid_turns": ["./cache/cacheAvoidTurns"],
    "cache_avoid_transp": ["./cache/cacheAvoidTransp"],
    "cache_avoid_blocking": ["./cache/cacheAvoidBlocking"]
    # Later:
    # "mpi": ["mpirun", "-np", "4", "./mpi/matmul"],
}

def generate_matrices(N, seed):

    rng = np.random.default_rng(seed)

    A = rng.random((N, N), dtype=np.float32)
    B = rng.random((N, N), dtype=np.float32)

    return A, B

def save_matrices(A, B):

    os.makedirs(DATA_DIR, exist_ok=True)

    # saving raw data as float32 binary files
    A.tofile(A_FILE)
    B.tofile(B_FILE)

    print(f"A saved: {A_FILE}")
    print(f"B saved: {B_FILE}")

# benchmarking function
def benchmark(command):

    times = []

    # Warmup
    for _ in range(WARMUP_RUNS):

        result = subprocess.run(
            command + [str(N), A_FILE, B_FILE],
            capture_output=True,
            text=True,
            check=True
        )

    # actual benchmarking
    for _ in range(RUNS):

        result = subprocess.run(
            command + [str(N), A_FILE, B_FILE],
            capture_output=True,
            text=True,
            check=True
        )

        # Programm has to output the time in seconds in the following format:
        #
        # TIME 0.123456
        #
        output = result.stdout.strip()

        if not output.startswith("TIME"):
            raise RuntimeError(
                f"Unerwartete Ausgabe:\n{output}"
            )

        time = float(output.split()[1])

        times.append(time)

    return times

# Results printing function
def print_results(name, times):

    # Calculate statistics
    median = np.median(times)
    minimum = np.min(times)
    mean = np.mean(times)
    std = np.std(times)

    flops = 2 * N**3

    median_gflops = flops / median / 1e9
    max_gflops = flops / minimum / 1e9

    print()
    print(name)
    print("-" * 40)

    print(f"Median:       {median:.6f} s")
    print(f"Minimum:      {minimum:.6f} s")
    print(f"Mean:         {mean:.6f} s")
    print(f"Std. dev.:    {std:.6f} s")

    print(f"Median:       {median_gflops:.2f} GFLOP/s")
    print(f"Maximum:      {max_gflops:.2f} GFLOP/s")

def main():

    print("=" * 60)
    print("Matrix Multiplication Benchmark")
    print("=" * 60)

    print(f"N:              {N}")
    print(f"Seed:           {SEED}")
    print(f"Warmup Runs:    {WARMUP_RUNS}")
    print(f"Benchmark Runs: {RUNS}")

    # generate matrices and save them to files
    A, B = generate_matrices(N, SEED)

    save_matrices(A, B)

    print()

    # benchmark each implementation
    for name, command in IMPLEMENTATIONS.items():

        executable = command[-1]

        if not os.path.exists(executable):
            print(f"{name}: skipped")
            print(f"Executable not found: {executable}")
            continue

        print()
        print(f"Benchmarking {name} ...")

        times = benchmark(command)

        print_results(name, times)


if __name__ == "__main__":
    main()