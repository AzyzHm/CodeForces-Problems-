#include <iostream>
#include <vector>

using namespace std;

int main() {
    long long n;
    cin >> n;
    long long even_sum = (n / 2) * ((n / 2) + 1);
    long long odd_sum = ((n + 1) / 2) * ((n + 1) / 2);
    long long f = even_sum - odd_sum;
    cout << f << endl;
    return 0;
}