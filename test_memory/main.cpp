#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sys/resource.h>

// #include PLACEHOLDER

template <typename T>
std::vector<T> read_input(const std::string& filename) {
    std::vector<T> data;
    std::ifstream infile(filename);
    T num;
    while (infile >> num) data.push_back(num);
    return data;
}

template <typename T>
void write_output(const std::string& filename, const std::vector<T>& data) {
    std::ofstream outfile(filename);
    for (const auto& num : data) outfile << num << " ";
    outfile << "\n";
}

double get_peak_memory_kb() {
    struct rusage usage;
    getrusage(RUSAGE_SELF, &usage);  // B on macOS, KB on Linux
    return usage.ru_maxrss / 1024.0;  // B → KB (macOS)
    // return usage.ru_maxrss;  // KB (Linux)
}

int main(int argc, char* argv[]) {

    double start_memory, vector_memory, sort_memory;

    start_memory = get_peak_memory_kb();

    std::vector<int> data = read_input<int>("../input/n0100000_random.txt");

    vector_memory = get_peak_memory_kb();

    // run_sort(data);
    
    sort_memory = get_peak_memory_kb();

    std::cout << vector_memory - start_memory << " "
              << sort_memory - vector_memory << std::endl;

    return 0;
}
