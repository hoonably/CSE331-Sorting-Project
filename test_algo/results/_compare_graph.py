import matplotlib.pyplot as plt
import matplotlib.cm as cm
import csv
import re
from collections import defaultdict
from pathlib import Path

# 설정
combined_csv = Path("csv/__combined_results.csv")
compare_path = Path("compare")
compare_path.mkdir(parents=True, exist_ok=True)

# 데이터 로딩
def load_combined_results(csv_path):
    results = defaultdict(dict)
    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            algo_name = row["algo_name"]
            fname = row["input_file"]
            try:
                time = float(row["time_sec"])
                acc = float(row["accuracy"])
                results[algo_name][fname] = (time, acc)
            except ValueError:
                continue
    return results

# 그래프 그리기
def plot_comparison(results, input_category):
    plt.figure(figsize=(10, 6))
    algorithms = list(results.keys())
    color_map = plt.get_cmap("tab20", len(algorithms))

    for idx, (algo_name, filedata) in enumerate(results.items()):
        series = []
        for filename, (time_sec, _) in filedata.items():
            match = re.match(r"n0*([0-9]+)_" + re.escape(input_category) + r"\.txt", filename)
            if not match:
                continue
            n = int(match.group(1))
            series.append((n, time_sec))

        if not series:
            continue

        series.sort()
        x = [n for n, _ in series]
        y = [t for _, t in series]
        plt.plot(x, y, marker='o', label=algo_name, color=color_map(idx))

    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (sec)")
    plt.title(f"Execution Time on {input_category} Input (All Algorithms)")
    plt.xscale("log")
    plt.yscale("log")
    plt.grid(True, which="major", linestyle="--")  # only major ticks
    plt.legend(loc="upper left", fontsize="small", ncol=2)
    plt.tight_layout()

    output_file = compare_path / f"{input_category}.png"
    plt.savefig(output_file, dpi=300)
    plt.close()
    return output_file

# 실행
if __name__ == "__main__":
    results = load_combined_results(combined_csv)
    CATEGORIES = ["sorted_asc", "sorted_desc", "random", "partial_50", "partial_80"]
    for cat in CATEGORIES:
        out = plot_comparison(results, cat)
        print(f"✅ Saved: {out}")
