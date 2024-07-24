#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solver(int n, int m, vector<int>& arr) {
    sort(arr.begin(), arr.end());
    int max_petals = 0;
    int current_sum = 0;
    int start = 0;

    for (int end = 0; end < n; ++end) {
        while (start < end && (arr[end] - arr[start] > 1 || current_sum + arr[end] > m)) {
            current_sum -= arr[start];
            start += 1;
        }

        if (current_sum + arr[end] <= m) {
            current_sum += arr[end];
            max_petals = max(max_petals, current_sum);
        } else {
            start += 1;
        }
    }

    return max_petals;
}

int main() {
    int t;
    vector<int> results;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        int n, m;
        cin >> n >> m;
        vector<int> arr(n);
        for (int j = 0; j < n; ++j) {
            cin >> arr[j];
        }
        results.push_back(solver(n, m, arr));
    }
    for (int i = 0; i < t; ++i) {
        cout << results[i] << endl;
    }
    return 0;
}