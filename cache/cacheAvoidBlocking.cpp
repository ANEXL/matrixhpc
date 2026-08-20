#include <iostream>
#include <fstream>
#include <algorithm>
#include <stdexcept>
#include <chrono>
#include <cstdlib>
using namespace std;

float* matmul(const float* A, const float* B, float* C, size_t N);
void read_matrix(const char* filename, float* matrix, size_t elements);

//Program to multiply two matrices but using blocking to avoid cache misses
int main(int argc, char* argv[])
{
    // Default matrix size and file names
    int input_N = (argc > 1) ? atoi(argv[1]) : 1024;
    if (input_N <= 0) {
        throw invalid_argument("Die Matrixdimension muss positiv sein.");
    }
    size_t N = static_cast<size_t>(input_N);
    const char* fileA = (argc > 2) ? argv[2] : "matrixA.bin";
    const char* fileB = (argc > 3) ? argv[3] : "matrixB.bin";

    // Calculate the number of elements in the matrices
    size_t elements = N * N;

    // Allocate memory for matrices A, B and C
    float* A = new float[elements];
    float* B = new float[elements];
    float* C = new float[elements];

    // Read matrices from binary files
    read_matrix(fileA, A, elements);
    read_matrix(fileB, B, elements);
    
    // Measure the time taken for matrix multiplication
    auto start = std::chrono::steady_clock::now();
    matmul(A, B, C, N);
    auto end = std::chrono::steady_clock::now();

    // Calculate the duration in seconds
    double duration = std::chrono::duration<double>(end - start).count();
    
    cout << "TIME " << duration << std::endl;
    return 0;
}

// Function to perform matrix multiplication but with blocking to avoid cache misses
float* matmul(const float* A, const float* B, float* C, size_t N)
{
    constexpr size_t block_size = 48;
    fill(C, C + N * N, 0.0f);

    for (size_t ii = 0; ii < N; ii += block_size) {
        for (size_t kk = 0; kk < N; kk += block_size) {
            for (size_t jj = 0; jj < N; jj += block_size) {
                const size_t i_end = min(ii + block_size, N);
                const size_t k_end = min(kk + block_size, N);
                const size_t j_end = min(jj + block_size, N);

                for (size_t i = ii; i < i_end; ++i) {
                    for (size_t k = kk; k < k_end; ++k) {
                        const float a = A[i * N + k];
                        for (size_t j = jj; j < j_end; ++j) {
                            C[i * N + j] += a * B[k * N + j];
                        }
                    }
                }
            }
        }
    }

    return C;
}

void read_matrix(const char* filename, float* matrix, size_t elements)
{
    std::ifstream file(
        filename,
        std::ios::binary
    );

    if (!file) {
        throw std::runtime_error(
            "Datei konnte nicht geöffnet werden."
        );
    }

    file.read(
        reinterpret_cast<char*>(matrix),
        elements * sizeof(float)
    );

    if (!file) {
        throw std::runtime_error(
            "Fehler beim Lesen der Matrix."
        );
    }
}