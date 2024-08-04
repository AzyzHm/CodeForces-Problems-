// not completed!
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

long solve(long a, long b, long c, long d) {
    if (a == c && b == d) return 0;
    if (b > d) return -1;

    if (a == b) {
        if (c > d) return -1;
        else return (d - b) + (d - c);
    }

    if (a < b) {
        if (c < d) return -1;
        else return (d - b) + abs(c - (a + (d - b)));
    }

    if (a > b) {
        if (d - b > (a - c)) return -1;
        else return (d - b) + (a - c);
    }

    return -1; // default case, should not reach here
}

int main(){
    int t;
    cin >> t;
    vector<int> results;
    for(int i = 0;i < t;++i){
        long a,b,c,d;
        cin >> a >> b >> c >> d;
        results.push_back(solve(a,b,c,d));
    }
    for(int i = 0;i < results.size();++i){
        cout << results[i] << endl;
    }
}