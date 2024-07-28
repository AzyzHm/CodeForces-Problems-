// solution incomplete
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <bitset>

using namespace std;

string to_binary(int n, int k) {
    string binary = bitset<32>(n).to_string(); // Convert to binary string
    return binary.substr(32 - k); // Get the last k bits
}

string add_zeros(string x, int n) {
    while (x.length() < n) {
        x = '0' + x;
    }
    return x;
}

string solve(int n, int k, int s, const vector<int>& a) {
    for (int i = *max_element(a.begin(), a.end())*60; i >= -1; --i) {
        int expression = 0;
        for (int j = 0; j < a.size(); ++j) {
            expression += i ^ a[j];
        }
        if (expression == s) {
            return add_zeros(to_binary(i, k), k);
        }
    }
    return "-1";
}

int main() {
    int t;
    cin >> t;
    vector<string> results;
    for (int _ = 0; _ < t; ++_) {
        int n, k;
        cin >> n >> k;
        string s_str;
        cin >> s_str;
        int s = stoi(s_str, nullptr, 2);
        vector<int> a(n);
        for (int i = 0; i < n; ++i) {
            string a_str;
            cin >> a_str;
            a[i] = stoi(a_str, nullptr, 2);
        }
        results.push_back(solve(n, k, s, a));
    }
    for (const string& result : results) {
        cout << result << endl;
    }
    return 0;
}