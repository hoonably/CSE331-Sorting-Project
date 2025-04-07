import csv
import re
import matplotlib.pyplot as plt
from collections import defaultdict

def load_results_from_csv(csv_path="benchmark_results.csv"):
    results = defaultdict(dict)
    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            algo = row["algorithm"]
            fname = row["input_file"]
            try:
                time = float(row["time_sec"])
                acc = float(row["accuracy"])
                results[algo][fname] = (time, acc)
            except ValueError:
                continue
    return results

def plot_random_input_comparison(results):
    plt.figure(figsize=(10, 6))
    
    for algo_name, filedata in results.items():
        series = []
        for filename, (time_sec, _) in filedata.items():
            if time_sec < 0:  # stack overflow
                continue
            match = re.match(r"n0*([0-9]+)_random\.txt", filename)
            if not match:
                continue
            n = int(match.group(1))
            series.append((n, time_sec))
        
        if not series:
            continue

        series.sort()
        x = [n for n, _ in series]
        y = [t for _, t in series]
        plt.plot(x, y, marker='o', label=algo_name)

    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (sec)")
    plt.title("Execution Time on Random Input (All Algorithms)")
    plt.xscale("log")
    plt.yscale("log")
    plt.grid(True, which="both", linestyle="--")
    plt.legend()
    plt.tight_layout()
    plt.savefig("../results/compare_random.png", dpi=300)
    plt.close()
    print("✅ Saved to ../results/compare_random.png")

if __name__ == "__main__":
    results = load_results_from_csv("../results/benchmark_results.csv")
    plot_random_input_comparison(results)
