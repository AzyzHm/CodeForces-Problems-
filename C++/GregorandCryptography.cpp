#include <iostream>
#include <vector>

using namespace std;

string solve(long long p){
    long long b = 3;
    while (b<=p){
        for (long long i = 2; i < b; i++) {
        if (p%i == p%b){
            return to_string(i) + " " + to_string(b);
        }
    }
    b++;
    }
    return "0 0";
}

int main(){
    int t;
    cin >> t;
    vector<string> results;
    for (int i = 0; i < t; ++i) {
        int n;
        cin >> n;
        results.push_back(solve(n));
    }
    for (const auto& result : results) {
        cout << result << endl;
    }
}