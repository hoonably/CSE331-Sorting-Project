/*
LIBRARY-SORT(A, ε = 0.5)
1 Allocate S[ (1 + ε) * n ], initialize to INF (unused)
2 Insert A[0] at center
3 For i = 1 to n-1:
4     Use binary search on valid elements to find logical position
5     Map logical index to physical position
6     Find nearest empty cell to that position (left/right)
7     If no gap: rebalance and retry
8     Else insert
9 Write back sorted result (skip INF)

Time Complexity:
  - Average Case: O(n log n)
  - Worst Case:   O(n^2)
Space Complexity:
  - O(n + εn) (gap included)
*/

#include <vector>
#include <limits>
#include <algorithm>
#include <cmath>
#include <climits>

const double EPSILON = 0.5;

template <typename T>
void rebalance(std::vector<T>& S, int filled) {
    T SENTINEL = std::numeric_limits<T>::max();
    std::vector<T> newS(S.size(), SENTINEL);

    // Extract valid elements
    std::vector<T> values;
    for (T x : S) {
        if (x != SENTINEL) values.push_back(x);
    }

    // Distribute with uniform gap
    int gap = S.size() / values.size();
    int pos = gap / 2;
    for (T val : values) {
        newS[pos] = val;
        pos += gap;
    }

    S = newS;
}

template <typename T>
void library_sort(std::vector<T>& A) {
    T SENTINEL = std::numeric_limits<T>::max();
    int n = A.size();
    int S_len = static_cast<int>(std::ceil((1.0 + EPSILON) * n));
    std::vector<T> S(S_len, SENTINEL);

    // Insert first element at center
    int mid = S_len / 2;
    S[mid] = A[0];
    int filled = 1;

    for (int i = 1; i < n; ++i) {
        // Step 1: collect valid elements with indices
        std::vector<T> values;
        std::vector<int> indices;
        for (int j = 0; j < S_len; ++j) {
            if (S[j] != SENTINEL) {
                values.push_back(S[j]);
                indices.push_back(j);
            }
        }

        // Step 2: find logical position via binary search
        T val = A[i];
        int pos = std::lower_bound(values.begin(), values.end(), val) - values.begin();

        // Step 3: map to physical position
        int phys_pos;
        if (pos == 0) {
            phys_pos = indices.empty() ? mid : indices.front() - 1;
        } else if (pos == (int)indices.size()) {
            phys_pos = indices.back() + 1;
        } else {
            phys_pos = (indices[pos - 1] + indices[pos]) / 2;
        }

        // Step 4: find nearest gap around phys_pos
        int left = phys_pos, right = phys_pos;
        while (left >= 0 && S[left] != SENTINEL) left--;
        while (right < S_len && S[right] != SENTINEL) right++;

        if (left >= 0) {
            S[left] = val;
        } else if (right < S_len) {
            S[right] = val;
        } else {
            rebalance(S, ++filled);
            i--; // retry same value
            continue;
        }

        filled++;
    }

    // Extract sorted result
    A.clear();
    for (T x : S) {
        if (x != SENTINEL)
            A.push_back(x);
    }
}
