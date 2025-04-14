
import subprocess
import time
import os
import csv

ALGORITHMS = {
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
    result = subprocess.run(["./temp_exec"], capture_output=True, text=True)
    output = result.stdout.strip()
    try:
        vals = list(map(float, output.split()))
        if len(vals) == 2:
            return vals  # vector, sort
        else:
            print(f"⚠️ Unexpected output format: '{output}'")
            return None
    except Exception as e:
        print(f"❌ Parse error: {e}, output: '{output}'")
        return None



def benchmark_memory():
    results = {}

    for algo_name, algo_cpp in ALGORITHMS.items():
        print(f"[+] Benchmarking memory for {algo_name}")
        if not compile_with_main(algo_name, algo_cpp):
            print(f"    ❌ Compile failed for {algo_name}")
            results[algo_name] = None
            continue

        warmup = run_once()  # warm-up
        if warmup is None:
            results[algo_name] = None
            continue

        stats = []  # [(vector, sort), ...]

        for _ in range(REPEAT):
            vals = run_once()
            if vals is None:
                print(f"    ❌ Measurement failed")
                break
            stats.append(vals)

        if len(stats) == REPEAT:
            # 평균 계산
            avg = [round(sum(col) / REPEAT, 2) for col in zip(*stats)]
            print(f"    📊 vector: {avg[0]} KB, sort: {avg[1]} KB")
            results[algo_name] = avg
        else:
            results[algo_name] = None

    return results


def save_to_csv(results):
    with open("results_memory.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["algorithm", "vector_kb", "sort_kb"])
        for algo, vals in results.items():
            if vals is not None:
                writer.writerow([algo] + vals)
            else:
                writer.writerow([algo, "ERROR", ""])
    print("📄 Saved results to results_memory.csv")


if __name__ == "__main__":
    results = benchmark_memory()
    save_to_csv(results)

    if os.path.exists(TEMP_MAIN): os.remove(TEMP_MAIN)
    if os.path.exists(TEMP_EXEC): os.remove(TEMP_EXEC)
