/*
LIBRARY-SORT(A)
1 Allocate S[ (1 + ε) * n ], initialize to GAP
2 Insert A[0] at center
3 For i = 1 to n-1:
4     Use binary search on valid elements to find logical position
5     Map logical index to physical position
6     Find nearest empty cell to that position (left/right)
7     If no gap: rebalance and retry
8     Else insert
9 Write back sorted result (skip GAPs)

Time Complexity:
  - Average Case: O(n log n)
  - Worst Case:   O(n^2)
Space Complexity:
  - O(n + εn) (gap included)
*/

#include <vector>
#include <cmath>
#include <limits>
#include <algorithm>

template <typename T>
class LibrarySorter {
public:
    explicit LibrarySorter(double epsilon = 0.5) : EPSILON(epsilon) {}

    void sort(std::vector<T>& A) {
        int n = A.size();
        int capacity = static_cast<int>((1.0 + EPSILON) * n);
        S.assign(capacity, sentinel());
        size = 0;

        // Insert first element in the middle
        int mid = capacity / 2;
        S[mid] = A[0];
        size++;

        for (int i = 1; i < n; ++i) {
            T val = A[i];

            // Extract valid elements
            std::vector<int> indices;
            for (int j = 0; j < capacity; ++j) {
                if (S[j] != sentinel())
                    indices.push_back(j);
            }

            std::vector<T> valid;
            for (int idx : indices)
                valid.push_back(S[idx]);

            int pos = std::lower_bound(valid.begin(), valid.end(), val) - valid.begin();
            int phys_pos;

            if (indices.empty()) {
                phys_pos = mid;
            } else if (pos == 0) {
                phys_pos = indices.front() - 1;
            } else if (pos == (int)indices.size()) {
                phys_pos = indices.back() + 1;
            } else {
                phys_pos = (indices[pos - 1] + indices[pos]) / 2;
            }

            int left = phys_pos, right = phys_pos;
            while (left >= 0 && S[left] != sentinel()) left--;
            while (right < capacity && S[right] != sentinel()) right++;

            if (left >= 0) {
                S[left] = val;
            } else if (right < capacity) {
                S[right] = val;
            } else {
                rebalance();
                --i;  // retry
                continue;
            }

            size++;
        }

        // Final compact copy
        A.clear();
        for (T x : S) {
            if (x != sentinel())
                A.push_back(x);
        }
    }

private:
    std::vector<T> S;
    int size = 0;
    const double EPSILON;

    void rebalance() {
        int new_capacity = S.size();
        std::vector<T> newS(new_capacity, sentinel());

        std::vector<T> valid;
        for (T x : S) {
            if (x != sentinel())
                valid.push_back(x);
        }

        int gap = new_capacity / valid.size();
        int pos = gap / 2;
        for (T val : valid) {
            newS[pos] = val;
            pos += gap;
        }

        S = newS;
    }

    T sentinel() const {
        return std::numeric_limits<T>::max();  // assumes T supports max and comparison
    }
};

// Global function wrapper
template <typename T>
void library_sort(std::vector<T>& A) {
    LibrarySorter<T> sorter;
    sorter.sort(A);
}
