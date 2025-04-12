# CSE331 Sorting Algorithm Benchmark Project

This project implements and benchmarks 12 classical and advanced sorting algorithms under consistent experimental conditions. It evaluates performance, memory usage, stability, and accuracy across various input types and data scales.

Author: Jeonghoon Park (20201118)  
UNIST, South Korea  
[GitHub Project Page](https://github.com/hoonably/CSE331-Sorting-Project)

---

## 🔍 Overview

Sorting is a fundamental operation in computer science. While classical algorithms like Merge Sort or Quick Sort are widely used, modern variants like Tim Sort and Intro Sort offer practical advantages in performance, adaptivity, and space complexity.

This project explores:

- Implementation of 12 sorting algorithms in C++
- Benchmarking across different input orders and data types
- Analysis of runtime, memory usage, stability, and accuracy

---

## 📁 Directory Structure

```bash
.
├── basic_sorting/            # Classical sorting algorithms
│   ├── bubble_sort.cpp
│   ├── heap_sort.cpp
│   ├── insertion_sort.cpp
│   ├── merge_sort.cpp
│   ├── quick_sort.cpp
│   ├── quick_sort_random.cpp
│   └── selection_sort.cpp
├── advanced_sorting/         # Advanced sorting algorithms
│   ├── cocktail_shaker_sort.cpp
│   ├── comb_sort.cpp
│   ├── intro_sort.cpp
│   ├── library_sort.cpp
│   ├── tim_sort.cpp
│   └── tournament_sort.cpp
├── test_algo/                # Main performance benchmarking (runtime)
│   ├── main.cpp
│   ├── benchmark.py
│   └── results/
├── test_memory/              # Memory usage benchmark
│   ├── main.cpp
│   ├── benchmark.py
│   └── results_memory.csv
├── test_stability/           # Stability testing
│   ├── main.cpp
│   ├── benchmark.py
│   ├── stability.csv
│   ├── input/
│   └── output/
├── test_type/                # Data type sensitivity benchmark
│   ├── main.cpp
│   ├── benchmark.py
│   └── results/
├── utils/                    # Input generation scripts
│   ├── input_generator.py
│   └── stability_input_generator.py
├── .gitignore
└── README.md                 # You're here!
```

---

## ⚙️ How to Run

This project includes four main experimental modules. Each one contains a C++ binary for core sorting logic and a Python script for benchmarking and logging results.

---

### 🔹 1. Algorithm Performance Benchmark (`test_algo`)

**Purpose**: Measure average runtime of 12 sorting algorithms on random and structured inputs of various sizes.

```bash
cd test_algo
python3 benchmark.py
```

Results will be saved in the `results/` directory.

---

### 🔹 2. Memory Usage Benchmark (`test_memory`)

**Purpose**: Measure peak memory usage (`ru_maxrss`) during execution of each sorting algorithm.

```bash
cd test_memory
python3 benchmark.py
```

Output will be stored in `results_memory.csv`.

---

### 🔹 3. Stability Analysis (`test_stability`)

**Purpose**: Test whether each algorithm preserves the relative order of equal elements (stability).

```bash
cd test_stability
python3 benchmark.py
```

- Input samples are in the `input/` folder  
- Sorted outputs are written to `output/`  
- Final stability report is saved as `stability.csv`

---

### 🔹 4. Data Type Sensitivity Benchmark (`test_type`)

**Purpose**: Evaluate how sorting performance changes with different numeric types (`int`, `long long`, `float`, `double`).

```bash
cd test_type
python3 benchmark.py
```

Results are stored in the `results/` directory.

---

### 📌 Prerequisites

- Python 3.x
- C++17 compatible compiler (e.g., `g++`, `clang++`)
- Tested on macOS and Linux (UNIX-like systems recommended)

---

## 📈 Implemented Algorithms

| Category  | Algorithms                                                                 |
|-----------|----------------------------------------------------------------------------|
| Basic     | Merge Sort, Heap Sort, Bubble Sort, Insertion Sort, Selection Sort, Quick Sort |
| Advanced  | Quick Sort (Random Pivot), Library Sort, Tim Sort, Comb Sort, Cocktail Shaker Sort, Tournament Sort, Intro Sort |

---

## 📊 Evaluation Metrics

- **Runtime**: average over 10 trials for each algorithm and input type
- **Input Sensitivity**: random, sorted, reverse-sorted, partially sorted
- **Data Type Support**: `int`, `long long`, `float`, `double`
- **Stability**: order preservation for equal elements
- **Memory Usage**: peak resident memory during sorting
- **Accuracy**: adjacent pair correctness after sorting

---

## 📝 Notes

- Sorting algorithms are implemented independently for consistency in benchmarking.
- All results, charts, and analysis are documented in the [final report PDF](./Sorting_Algorithm_Analysis_and_Implementation.pdf).
- Library Sort was modified following Faujdar & Ghrera (2015) for improved performance.

---

## 📜 License

This project is part of CSE331 coursework at UNIST.  
Use for educational and research purposes only.

