#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

string solve(string s, const vector<long>& a, int n) {
    if (s.size() != n) return "NO";
    
    unordered_map<long, char> num_to_char;
    unordered_map<char, long> char_to_num;
    
    for (int i = 0; i < n; ++i) {
        if (num_to_char.count(a[i])) {
            if (num_to_char[a[i]] != s[i]) return "NO";
        } else {
            num_to_char[a[i]] = s[i];
        }

        if (char_to_num.count(s[i])) {
            if (char_to_num[s[i]] != a[i]) return "NO";
        } else {
            char_to_num[s[i]] = a[i];
        }
    }
    
    return "YES";
}

int main() {
    int t;
    cin >> t;
    vector<string> results;
    
    for (int i = 0; i < t; ++i) {
        long n;
        cin >> n;
        vector<long> a(n);
        
        for (long &x : a) cin >> x;
        
        long m;
        cin >> m;
        
        for (int j = 0; j < m; ++j) {
            string s;
            cin >> s;
            results.push_back(solve(s, a, n));
        }
    }
    
    for (const string& result : results) {
        cout << result << endl;
    }
    
    return 0;
}
