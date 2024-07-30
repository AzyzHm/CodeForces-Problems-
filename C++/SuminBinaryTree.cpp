#include <iostream>
#include <vector>

using namespace std;

int main(){
    int t;
    cin >> t;
    vector<long long> results;
    for (int i = 0;i<t;++i){
        long long n;
        cin >> n;
        long long result = 0;
        while (n>0){
            result += n;
            n /= 2;
        }
        results.push_back(result);
    }
    for (int i = 0;i<t;++i){
        cout << results[i] << endl;
    }
}