import subprocess
import time
import os
from pathlib import Path
from collections import defaultdict
import csv

ALGORITHMS = {
    "merge_sort": "basic_sorting/merge_sort.cpp",
    "heap_sort": "basic_sorting/heap_sort.cpp",
    "bubble_sort": "basic_sorting/bubble_sort.cpp",
    "insertion_sort": "basic_sorting/insertion_sort.cpp",
    "selection_sort": "basic_sorting/selection_sort.cpp",
    "quick_sort": "basic_sorting/quick_sort.cpp",
    # "library_sort": "advanced_sorting/library_sort.cpp",
    # "tim_sort": "advanced_sorting/tim_sort.cpp",
    # "cocktail_sort": "advanced_sorting/cocktail_sort.cpp",
    # "comb_sort": "advanced_sorting/comb_sort.cpp",
    # "tournament_sort": "advanced_sorting/tournament_sort.cpp",
    # "introsort": "advanced_sorting/introsort.cpp",
}

INPUT_DIR = "../input"
OUTPUT_DIR = "../output"
MAIN_TEMPLATE = "../tests/main.cpp"
TEMP_MAIN = "../tests/temp_main.cpp"
TEMP_EXEC = "../tests/temp_exec"
REPEAT = 10

def run_once(exe_path, input_file, output_file):
    result = subprocess.run(
        [exe_path, input_file, output_file],
        capture_output=True,
        text=True
    )
    try:
        return float(result.stdout.strip())
    # Stack Overflow or other error
    except ValueError:
        return -1

def accuracy_score_file(filename):
    with open(filename, 'r') as f:
        try:
            nums = list(map(int, f.read().strip().split()))
        except ValueError:
            return 0.0
    if len(nums) <= 1:  # if the file is empty or has only one number
        return 1.0
    violations = sum(1 for i in range(len(nums) - 1) if nums[i] > nums[i + 1])
    score = 1.0 - (violations / (len(nums) - 1))
    return round(score, 4)

def compile_with_main(algo_name, algo_path):
    with open(MAIN_TEMPLATE, 'r') as f:
        code = f.read()
    code = code.replace("// #include PLACEHOLDER", f'#include "../{algo_path}"')  # include line
    code = code.replace("// run_sort(data);", f"{algo_name}(data);")  # function call

    with open(TEMP_MAIN, 'w') as f:
        f.write(code)

    result = subprocess.run(["g++", "-O2", "-std=c++17", "-o", TEMP_EXEC, TEMP_MAIN])
    return result.returncode == 0

def warmup_io(input_path, output_path):
    subprocess.run([f"./{TEMP_EXEC}", input_path, output_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def benchmark_all():
    results = defaultdict(dict)
    input_files = sorted(f for f in os.listdir(INPUT_DIR) if f.endswith(".txt"))

    for algo_name, algo_cpp in ALGORITHMS.items():
        print(f"\n[+] Benchmarking {algo_name}")

        if not compile_with_main(algo_name, algo_cpp):
            print(f"    ❌ Compile failed for {algo_name}")
            continue

        algo_output_dir = os.path.join(OUTPUT_DIR, algo_name)
        os.makedirs(algo_output_dir, exist_ok=True)

        for input_file in input_files:
            input_path = os.path.join(INPUT_DIR, input_file)
            output_file = os.path.join(algo_output_dir, input_file)

            time_list = []
            acc_list = []

            warmup_io(input_path, output_file)  # Warmup run to avoid cold start

            is_stack_overflow = False
            rep = 0
            for rep in range(REPEAT):
                rep += 1
                elapsed = run_once(f"./{TEMP_EXEC}", input_path, output_file)

                # Stack Overflow
                if elapsed == -1:
                    is_stack_overflow = True
                    break
                        
                accuracy = accuracy_score_file(output_file)
                time_list.append(elapsed)
                acc_list.append(accuracy)
                
                # if it takes too long, we just use the first result
                # We already have a warmup run, so this is not a problem
                if elapsed > 60:  
                    break

            if is_stack_overflow: 
                print(f"    {input_file}: ❌ Stack Overflow")
                results[algo_name][input_file] = (-1, -1)
            else:
                median_time = round(sum(time_list) / rep, 6)
                avg_accuracy = round(sum(acc_list) * 100 / rep, 4)
                print(f"    {input_file}: {median_time:.6f} sec, Accuracy: {avg_accuracy:.4f}%")
                results[algo_name][input_file] = (median_time, avg_accuracy)

    return results

def save_results_to_csv(results, csv_path="../results/benchmark_results.csv"):
    with open(csv_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["algorithm", "input_file", "time_sec", "accuracy"])
        for algo, inputs in results.items():
            for input_file, (time_sec, accuracy) in inputs.items():
                writer.writerow([
                    algo,
                    input_file,
                    f"{time_sec:.6f}",
                    f"{accuracy:.4f}"
                ])
    print(f"📄 Results saved to {csv_path}")


if __name__ == "__main__":
    
    results = benchmark_all()
    save_results_to_csv(results)

    if os.path.exists(TEMP_MAIN):
        os.remove(TEMP_MAIN)
    if os.path.exists(TEMP_EXEC):
        os.remove(TEMP_EXEC)