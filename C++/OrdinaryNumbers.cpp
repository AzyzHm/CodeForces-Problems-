#include <iostream>
#include <vector>

using namespace std;

int countIdenticalDigits(int n) {
    int count = 0;
    for (int i = 1; i <= 9; i++) {
        long long identicalNum = i;
        while (identicalNum <= n) {
            count++;
            identicalNum = identicalNum * 10 + i;
        }
    }

    return count;
}

int main() {
    int t;
    cin >> t;
    vector<int> results(t);

    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;
        results[i] = countIdenticalDigits(n);
    }

    for (const int& result : results) {
        cout << result << endl;
    }

    return 0;
}