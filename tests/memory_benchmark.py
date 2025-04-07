import subprocess
import time
import os
import psutil
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

def run_once_memory(exe_path, input_file):
    proc = subprocess.Popen([exe_path, input_file, OUTPUT_FILE])
    p = psutil.Process(proc.pid)

    peak_memory = 0
    try:
        while proc.poll() is None:
            mem = p.memory_info().rss
            peak_memory = max(peak_memory, mem)
            time.sleep(0.01)
    except psutil.NoSuchProcess:
        pass
    return peak_memory / (1024 * 1024)  # bytes → MB

def benchmark_all_memory():
    results = defaultdict(dict)

    input_files = sorted(f for f in os.listdir(INPUT_DIR) if f.endswith(".txt"))

    for algo_name, exe_path in ALGORITHMS.items():
        print(f"\n[+] Memory Benchmark: {algo_name}")
        for input_file in input_files:
            input_path = os.path.join(INPUT_DIR, input_file)
            mem_usages = [run_once_memory(exe_path, input_path) for _ in range(REPEAT)]
            avg_memory = sum(mem_usages) / REPEAT
            print(f"    {input_file}: {avg_memory:.2f} MB")
            results[algo_name][input_file] = avg_memory
    return results

if __name__ == "__main__":
    benchmark_all_memory()
