#include <iostream>
#include <vector>

using namespace std;

string solve(int n,vector<int> v){
    if (v[n-1] >= v[0] + v[1]) {
        return "1 2 " + to_string(n);
    } else {
        return "-1";
    }
}
int main(){
    int t;
    cin >> t;
    vector <string> results;
    for(int i = 0;i < t;++i){
        int n;
        cin >> n;
        vector <int> v(n);
        for(int j = 0;j < n;++j){
            cin >> v[j];
        }
        results.push_back(solve(n,v));
    }
    for(int k = 0;k < results.size();++k){
        cout << results[k] << endl;
    }
}