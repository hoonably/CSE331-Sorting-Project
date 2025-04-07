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

- `basic_sorting/`: Conventional sorting algorithms (implemented from scratch)
- `advanced_sorting/`: Modern sorting algorithms with pseudocode reference
- `utils/`: Input generation, timing tools, and plot functions
- `tests/`: Scripts to run experiments and validate sorting correctness
- `report/`: ACM format LaTeX report (see `sample-sigconf.tex`)

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/CSE331-Sorting-Project.git
   cd CSE331-Sorting-Project
   ```

2. Install required packages (optional for plotting):
   ```bash
   pip install matplotlib
   ```

3. Run test runner to benchmark all algorithms:
   ```bash
   python tests/test_runner.py
   ```

## 🧪 Dataset Types

The following input sequences are tested:

- Sorted (ascending)
- Sorted (descending)
- Random
- Partially sorted

Each test is executed 10 times to compute the average execution time.

## 📄 Report

The full analysis is documented in [`report/sample-sigconf.tex`](report/sample-sigconf.tex), written in ACM sigconf format.