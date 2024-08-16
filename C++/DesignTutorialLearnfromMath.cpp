#include <iostream>
#include <vector>

using namespace std;

bool isComposite(int num) {
    if (num < 4) {
        return false;
    }
    for (int i = 2; i <= num / 2; i++) {
        if (num % i == 0) {
            return true;
        }
    }
    return false;
}

int main() {
    int n;
    cin >> n;

    for (int i = 4; i <= n / 2; i++) {
        if (isComposite(i) && isComposite(n - i)) {
            cout << i << " " << n - i << endl;
            break;
        }
    }

    return 0;
}