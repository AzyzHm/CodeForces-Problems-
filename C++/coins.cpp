#include <iostream>
#include <vector>

using namespace std;

string solve(long long n,long long k){
    if((n%k)%2 == 0 || n%2 == 0 || (n-k)%2 == 0)return "Yes";
    else return "No";
}

int main(){
    int t;
    cin >> t;
    vector<string> results;
    for(int i = 0; i < t;++i){
        long long n,k;
        cin >> n >> k ;
        results.push_back(solve(n,k));
    }
    for(int j = 0;j < results.size();++j){
        cout << results[j] << endl;
    }
}