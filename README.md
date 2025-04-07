# CSE331 - Sorting Algorithm Analysis and Implementation

This repository contains the source code, dataset generators, and experimental scripts for Assignment #1 in CSE331: Introduction to Algorithms (2025, UNIST). The goal of this assignment is to implement, analyze, and compare the performance of 12 different sorting algorithms.

## 📌 Objectives

- Implement 6 conventional comparison-based sorting algorithms
- Implement 6 contemporary/modern sorting algorithms
- Analyze each algorithm's design, time complexity, and stability
- Generate various input datasets (random, sorted, reversed, partially sorted)
- Evaluate execution time, memory usage, and correctness
- Present results in a structured report following the ACM sigconf format

## 🔧 Implemented Algorithms

### Basic Sorting Algorithms (Comparison-based)

- Merge Sort
- Heap Sort
- Bubble Sort
- Insertion Sort
- Selection Sort
- Quick Sort

### Advanced Sorting Algorithms (Modern)

- Library Sort
- Tim Sort
- Cocktail Shaker Sort
- Comb Sort
- Tournament Sort
- Introsort

## 📁 Repository Structure

- `basic_sorting/`  
  Conventional sorting algorithms implemented from scratch:  
  - Bubble Sort, Insertion Sort, Selection Sort  
  - Merge Sort, Quick Sort, Heap Sort

- `advanced_sorting/`  
  Advanced or modern sorting algorithms based on theoretical pseudocode:  
  - Tim Sort, Introsort, Library Sort  
  - Comb Sort, Cocktail Shaker Sort, Tournament Sort

- `input/`  
  Generated input files of various sizes and types:  
  - Sizes: 1,000 ~ 1,000,000  
  - Types: random, sorted, reverse-sorted, partially sorted (50%, 80%)

- `output/`  
  Output files from sorting executions, organized per algorithm

- `results/`  
  Aggregated benchmark results and generated plots:  
  - `benchmark_results.csv`: execution time & accuracy per input  
  - `.png`: log-log plot of time vs. input size by type

- `tests/`  
  Experimental framework:
  - `benchmark.py`: compiles and evaluates all algorithms
  - `main.cpp`: universal main function for measuring execution
  - Generates temporary executables to test individual sorts

- `utils/`  
  Support tools:  
  - `generator.py`: creates sorted/unsorted input sets  
  - `make_graph.py`: visualizes benchmark results from CSV  

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/hoonably/CSE331-Sorting-Project.git
   cd CSE331-Sorting-Project
   ```

2. Install required packages (optional for plotting):
   ```bash
   pip install matplotlib
   ```

3. Run test runner to benchmark all algorithms:
   ```bash
   cd tests
   python3 benchmark.py
   ```

## 🧪 Dataset Types

The following input sequences are tested:

- Sorted (ascending)
- Sorted (descending)
- Random
- Partially sorted (50%, 80%)  

How to test:

- Each test is repeated up to 10 times.
- If any run exceeds 60 seconds, the test stops early and uses the average of completed runs.
- Sorting accuracy and time are measured separately.

## 📄 Data & Report

- Graphs saved to: `results/{algorithm_name}.png` (log-log scale)
- The full analysis is documented in [`report/20201118.tex`](report/20201118.tex), written in ACM sigconf format.