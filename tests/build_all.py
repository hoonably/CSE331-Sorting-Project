import subprocess
import os

CPP_SOURCES = {
    "merge_sort": "basic_sorting/merge_sort.cpp",
    "heap_sort": "basic_sorting/heap_sort.cpp",
    "bubble_sort": "basic_sorting/bubble_sort.cpp",
    "insertion_sort": "basic_sorting/insertion_sort.cpp",
    "selection_sort": "basic_sorting/selection_sort.cpp",
    "quick_sort": "basic_sorting/quick_sort.cpp",
    "library_sort": "advanced_sorting/library_sort.cpp",
    "tim_sort": "advanced_sorting/tim_sort.cpp",
    "cocktail_sort": "advanced_sorting/cocktail_sort.cpp",
    "comb_sort": "advanced_sorting/comb_sort.cpp",
    "tournament_sort": "advanced_sorting/tournament_sort.cpp",
    "introsort": "advanced_sorting/introsort.cpp",
}

def build_all():
    for name, src_path in CPP_SOURCES.items():
        out_path = src_path.replace(".cpp", "")
        print(f"[+] Building {name}...")
        result = subprocess.run(["g++", "-O2", "-std=c++17", "-o", out_path, src_path])
        if result.returncode != 0:
            print(f"    ❌ Failed to compile {name}")
        else:
            print(f"    ✅ Compiled {out_path}")

if __name__ == "__main__":
    build_all()
