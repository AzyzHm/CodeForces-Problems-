#include <iostream>
#include <vector>
#include <set>

using namespace std;

bool check_exist(vector<char> v, const set<vector<char>>& combinations) {
    return combinations.find(v) != combinations.end();
}

int solve(int n, string s) {
    set<vector<char>> combinations;
    for (int i = 0; i < n - 1; ++i) {
        vector<char> v = {s[i], s[i + 1]};
        combinations.insert(v);
    }
    return combinations.size();
}

int main() {
    int t;
    cin >> t;
    vector<int> results;
    for (int i = 0; i < t; ++i) {
        int n;
        cin >> n;
        string s;
        cin >> s;
        results.push_back(solve(n, s));
    }
    for (int i = 0; i < t; ++i) {
        cout << results[i] << endl;
    }
    return 0;
}