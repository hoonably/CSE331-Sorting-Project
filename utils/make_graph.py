# This script generates plots from the benchmark results stored in a CSV file.

import csv
from collections import defaultdict
import matplotlib.pyplot as plt
import re

def load_results_from_csv(csv_path="benchmark_results.csv"):
    results = defaultdict(dict)
    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            algo = row["algorithm"]
            fname = row["input_file"]
            try:
                time = float(row["avg_time"])
                acc = float(row["accuracy"])
                results[algo][fname] = (time, acc)
            except ValueError:
                continue
    return results

def plot_by_input_type(results, algo_name):
    categories = ["sorted_asc", "sorted_desc", "random", "partial_50", "partial_80"]
    series = {cat: [] for cat in categories}
    sizes = set()

    for filename, (time_sec, _) in results[algo_name].items():
        if time_sec < 0:  # stack overflow
            continue
        match = re.match(r"n0*([0-9]+)_(.+)\.txt", filename)
        if not match:
            continue
        n = int(match.group(1))
        kind = match.group(2)
        if kind in series:
            series[kind].append((n, time_sec))
            sizes.add(n)

    sizes = sorted(sizes)

    plt.figure(figsize=(10, 6))
    for kind, data in series.items():
        if not data:
            continue
        data.sort()  # ensure increasing x
        x = [n for n, _ in data]
        y = [t for _, t in data]
        plt.plot(x, y, marker='o', label=kind)

    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (sec)")
    plt.title(f"Execution Time by Input Type: {algo_name}")
    plt.xscale("log")
    plt.yscale("log")
    plt.grid(True, which="both", ls="--")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"../results/{algo_name}.png", dpi=300)
    plt.close()

# Save at ../results/{algo_name}.png
def plot_all_algorithms(results):
    for algo_name in results:
        print(f"\n📊 Plotting: {algo_name}")
        plot_by_input_type(results, algo_name)

if __name__ == "__main__":
    results = load_results_from_csv("../tests/benchmark_results.csv")
    plot_all_algorithms(results)
