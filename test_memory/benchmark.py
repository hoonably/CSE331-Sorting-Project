
import subprocess
import time
import os
import csv

ALGORITHMS = {
    "vector_only": None,  # No algorithm, just vector usage
    "merge_sort": "basic_sorting/merge_sort.cpp",
    "heap_sort": "basic_sorting/heap_sort.cpp",
    "bubble_sort": "basic_sorting/bubble_sort.cpp",
    "insertion_sort": "basic_sorting/insertion_sort.cpp",
    "selection_sort": "basic_sorting/selection_sort.cpp",
    "quick_sort": "basic_sorting/quick_sort.cpp",
    "quick_sort_random": "basic_sorting/quick_sort_random.cpp",
    "library_sort": "advanced_sorting/library_sort.cpp",
    "tim_sort": "advanced_sorting/tim_sort.cpp",
    "cocktail_shaker_sort": "advanced_sorting/cocktail_shaker_sort.cpp",
    "comb_sort": "advanced_sorting/comb_sort.cpp",
    "tournament_sort": "advanced_sorting/tournament_sort.cpp",
    "intro_sort": "advanced_sorting/intro_sort.cpp",
}

MAIN_TEMPLATE = "main.cpp"
TEMP_MAIN = "temp_main.cpp"
TEMP_EXEC = "temp_exec"
REPEAT = 10

def compile_with_main(algo_name, algo_path):
    with open(MAIN_TEMPLATE, 'r') as f:
        code = f.read()
    if algo_path is not None:  # if algo_path is None, we are using vector_only
        code = code.replace("// #include PLACEHOLDER", f'#include "../{algo_path}"')
        code = code.replace("// run_sort(data);", f"{algo_name}(data);")
    with open(TEMP_MAIN, 'w') as f:
        f.write(code)
    result = subprocess.run(["g++", "-O2", "-std=c++17", "-o", TEMP_EXEC, TEMP_MAIN])
    return result.returncode == 0

def run_once():
    result = subprocess.run(
        [f"./{TEMP_EXEC}"],
        capture_output=True, text=True
    )
    try:
        values = result.stdout.strip().split()
        if len(values) >= 1:
            return int(values[0])
        else:
            return -1
    except ValueError:
        return -1

def benchmark_memory():
    results = {}

    for algo_name, algo_cpp in ALGORITHMS.items():
        print(f"[+] Benchmarking memory for {algo_name}")
        if not compile_with_main(algo_name, algo_cpp):
            print(f"    ❌ Compile failed for {algo_name}")
            results[algo_name] = -1
            continue
        
        run_once()  # Warm-up run to avoid cold start

        mem_list = []
        for _ in range(REPEAT):
            peak_mb = run_once()
            if peak_mb == -1:
                print(f"    ❌ Measurement failed")
                break
            mem_list.append(peak_mb)

        if len(mem_list) == REPEAT:
            avg_mem = round(sum(mem_list) / REPEAT, 2)
            print(f"    📈 Peak Memory: {avg_mem} MB")
            results[algo_name] = avg_mem
        else:
            results[algo_name] = -1

    return results

def save_to_csv(results):
    with open("results_memory.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["algorithm", "peak_memory_mb"])
        for algo, mem in results.items():
            writer.writerow([algo, mem])
    print("📄 Saved results to results_memory.csv")

if __name__ == "__main__":
    results = benchmark_memory()
    save_to_csv(results)

    if os.path.exists(TEMP_MAIN): os.remove(TEMP_MAIN)
    if os.path.exists(TEMP_EXEC): os.remove(TEMP_EXEC)
