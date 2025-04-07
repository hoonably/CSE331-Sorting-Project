#include <iostream>
#include <fstream>
#include <vector>
#include <string>
// #include PLACEHOLDER

std::vector<int> read_input(const std::string& filename) {
    std::vector<int> data;
    std::ifstream infile(filename);
    int num;
    while (infile >> num) data.push_back(num);
    return data;
}

void write_output(const std::string& filename, const std::vector<int>& data) {
    std::ofstream outfile(filename);
    for (int num : data) outfile << num << " ";
    outfile << "\n";
}

int main(int argc, char* argv[]) {
    std::vector<int> data = read_input(argv[1]);
    
    auto start = std::chrono::high_resolution_clock::now();
    // run_sort(data);  // This will be {algo_name}(data);
    auto end = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double> elapsed = end - start;
    std::cout << elapsed.count() << std::endl;  // Print elapsed time

    write_output(argv[2], data);
    return 0;
}
