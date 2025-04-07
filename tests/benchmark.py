import subprocess
import time
import os
from collections import defaultdict

ALGORITHMS = {
    "merge_sort": "./basic_sorting/merge_sort",
    "heap_sort": "./basic_sorting/heap_sort",
    "bubble_sort": "./basic_sorting/bubble_sort",
    "insertion_sort": "./basic_sorting/insertion_sort",
    "selection_sort": "./basic_sorting/selection_sort",
    "quick_sort": "./basic_sorting/quick_sort",
    "library_sort": "./advanced_sorting/library_sort",
    "tim_sort": "./advanced_sorting/tim_sort",
    "cocktail_sort": "./advanced_sorting/cocktail_sort",
    "comb_sort": "./advanced_sorting/comb_sort",
    "tournament_sort": "./advanced_sorting/tournament_sort",
    "introsort": "./advanced_sorting/introsort",
}

INPUT_DIR = "input"
OUTPUT_FILE = "output/temp.txt"
REPEAT = 10

def run_once(exe_path, input_file):
    start = time.perf_counter()
    subprocess.run([exe_path, input_file, OUTPUT_FILE], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    end = time.perf_counter()
    return end - start

def accuracy_score_file(filename):
    with open(filename, 'r') as f:
        try:
            nums = list(map(int, f.read().strip().split()))
        except ValueError:
            return 0.0
    if len(nums) <= 1:
        return 1.0
    violations = sum(1 for i in range(len(nums) - 1) if nums[i] > nums[i + 1])
    score = 1.0 - (violations / (len(nums) - 1))
    return round(score, 4)

def benchmark_all():
    results = defaultdict(dict)
    input_files = sorted(f for f in os.listdir(INPUT_DIR) if f.endswith(".txt"))

    for algo_name, exe_path in ALGORITHMS.items():
        print(f"\n[+] Benchmarking {algo_name}")
        for input_file in input_files:
            input_path = os.path.join(INPUT_DIR, input_file)

            time_list = []
            acc_list = []

            for _ in range(REPEAT):
                elapsed = run_once(exe_path, input_path)
                accuracy = accuracy_score_file(OUTPUT_FILE)
                time_list.append(elapsed)
                acc_list.append(accuracy)

            avg_time = sum(time_list) / REPEAT
            avg_accuracy = sum(acc_list) / REPEAT

            print(f"    {input_file}: {avg_time:.6f} sec, Accuracy: {avg_accuracy:.4f}")
            results[algo_name][input_file] = (avg_time, avg_accuracy)

    return results

if __name__ == "__main__":
    benchmark_all()
