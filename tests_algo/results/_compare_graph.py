import csv
import re
import matplotlib.pyplot as plt
from collections import defaultdict
from pathlib import Path

def load_all_results_from_folder(folder_path):
    results = defaultdict(dict)
    folder = Path(folder_path)
    csv_files = folder.glob("*.csv")

    for csv_file in csv_files:
        algo_name = csv_file.stem
        with open(csv_file, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                fname = row["input_file"]
                try:
                    time = float(row["time_sec"])
                    acc = float(row["accuracy"])
                    results[algo_name][fname] = (time, acc)
                except ValueError:
                    continue
    return results

def plot_random_input_comparison(results, input):
    plt.figure(figsize=(10, 6))
    
    for algo_name, filedata in results.items():
        series = []
        for filename, (time_sec, _) in filedata.items():
            match = re.match(r"n0*([0-9]+)_" + re.escape(input) + r"\.txt", filename)
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
    plt.title(f"Execution Time on {input} Input (All Algorithms)")
    plt.xscale("log")
    plt.yscale("log")
    plt.grid(True, which="both", linestyle="--")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"compare/{input}.png", dpi=300)
    plt.close()
    print(f"✅ Saved to compare/{input}.png")

if __name__ == "__main__":
    results = load_all_results_from_folder("csv")
    CATEGORIES = ["sorted_asc", "sorted_desc", "random", "partial_50", "partial_80"]
    for input in CATEGORIES:
        plot_random_input_comparison(results, input)
