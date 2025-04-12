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

long get_peak_memory_kb() {
    struct rusage usage;
    getrusage(RUSAGE_SELF, &usage);
    return usage.ru_maxrss; // KB on Linux/macOS
}

int main(int argc, char* argv[]) {

    long peak_memory = 0;

    std::vector<int> data = read_input<int>("../input/n0100000_random.txt");
    // run_sort(data);
    

    peak_memory = 1.0 * get_peak_memory_kb() / 1024; // Convert to MB
    std::cout << peak_memory << std::endl;
    return 0;
}
