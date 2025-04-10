import csv
from collections import defaultdict

INPUT_FILE = "__combined_results.csv"
OUTPUT_FILE = "__pivot_table.csv"

def generate_pivot_table():
    data = defaultdict(dict)
    types = set()
    algorithms = set()

    with open(INPUT_FILE, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            algo = row["algorithm"]
            typ = row["type"]
            time = float(row["time_sec"])

            data[algo][typ] = f"{time:.6f}"
            types.add(typ)
            algorithms.add(algo)

    types = sorted(types)
    algorithms = sorted(algorithms)

    with open(OUTPUT_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["algorithm"] + types)

        for algo in algorithms:
            row = [algo]
            for typ in types:
                row.append(data[algo].get(typ, ""))
            writer.writerow(row)

    print(f"✅ Pivot table saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_pivot_table()
