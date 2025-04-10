# Make graphs from CSV files

import os
import csv
import re
import matplotlib.pyplot as plt

CATEGORIES = ["sorted_asc", "sorted_desc", "random", "partial_50", "partial_80"]

def load_csv(filepath):
    data = {cat: [] for cat in CATEGORIES}
    with open(filepath, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            fname = row["input_file"]
            try:
                time = float(row["time_sec"])
            except ValueError:
                continue

            match = re.match(r"n0*([0-9]+)_(.+)\.txt", fname)
            if not match:
                continue
            n = int(match.group(1))
            kind = match.group(2)
            if kind in data:
                data[kind].append((n, time))
    return data

def plot_one_algorithm(csv_path):
    algo_name = os.path.splitext(os.path.basename(csv_path))[0]
    print(f"📊 Plotting {algo_name}...")

    series = load_csv(csv_path)

    plt.figure(figsize=(10, 6))
    for kind, points in series.items():
        if not points:
            continue
        points.sort()
        x = [n for n, _ in points]
        y = [t for _, t in points]
        plt.plot(x, y, marker='o', label=kind)

    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (sec)")
    plt.title(f"Execution Time by Input Type: {algo_name}")
    plt.xscale("log")
    plt.yscale("log")
    plt.grid(True, which="both", linestyle="--")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{"graph"}/{algo_name}.png", dpi=300)
    plt.close()

def plot_all():
    for filename in os.listdir("csv"):
        if filename.endswith(".csv"):
            plot_one_algorithm(os.path.join("csv", filename))

if __name__ == "__main__":
    plot_all()
