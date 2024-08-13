#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

bool check_seats(const unordered_set<int>& seat_set, int b) {
    return seat_set.count(b + 1) > 0 || seat_set.count(b - 1) > 0;
}

int main() {
    int t;
    cin >> t;
    vector<string> results;

    for (int i = 0; i < t; ++i) {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int j = 0; j < n; ++j) {
            cin >> a[j];
        }
        unordered_set<int> seat_set;
        seat_set.insert(a[0]);
        string res = "YES";
        for (int k = 1; k < n; ++k) {
            if (check_seats(seat_set, a[k])) {
                seat_set.insert(a[k]);
            } else {
                res = "NO";
                break;
            }
        }
        results.push_back(res);
    }
    for (const auto& result : results) {
        cout << result << endl;
    }
}