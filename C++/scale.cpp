#include <iostream>
#include <vector>
#include <string>

using namespace std;

string solve(int n, int k, const vector<vector<char>>& a) {
    string solution = "";
    int i = 0;
    int j = 0;
    while (i < n) {
        while (j < n) {
            if (i % k == 0 && j % k == 0) {
                solution += a[i][j];
            }
            j += k;
        }
        if (i != n - k) {
            solution += "\n";
        }
        i += k;
        j = 0;
    }
    return solution;
}

int main() {
    int t;
    cin >> t;
    vector<string> results;
    for (int _ = 0; _ < t; ++_) {
        int n, k;
        cin >> n >> k;
        vector<vector<char>> a(n, vector<char>(n));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                cin >> a[i][j];
            }
        }
        results.push_back(solve(n, k, a));
    }
    for (const string& r : results) {
        cout << r << endl;
    }
    return 0;
}