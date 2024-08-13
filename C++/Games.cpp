#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> hi(n), ai(n);
    for (int i = 0; i < n; i++) {
        cin >> hi[i] >> ai[i];
    }

    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i != j && hi[i] == ai[j]) {
                count++;
            }
        }
    }

    cout << count << endl;
    return 0;
}