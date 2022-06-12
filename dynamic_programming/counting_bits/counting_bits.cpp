#include <cmath>

class Solution {
private:
    int recursive_count_bits(int n, const vector<int> &previous_solutions) {
        // base case
        if (n==0)
            return 0;
        else {
            int number_without_MSB = n-int(std::pow(2, int(std::log2(n))));
            int solution_without_MSB = previous_solutions[number_without_MSB];
            return 1+solution_without_MSB;
        }
    }

public:
    vector<int> countBits(int n) {
        vector<int> solutions;
        solutions.reserve(n+1);
        for (int i=0; i<=n; ++i) {
            solutions.push_back(recursive_count_bits(i, solutions));
        }
        return solutions;
    }
};