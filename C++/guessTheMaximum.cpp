#include <iostream>
#include <vector>

using namespace std;
int max(int a,int b){
    if(a>b)return a;
    else return b;
}

int solve(int n,vector<int> v){
    int min = max(v[0],v[1]);
    for (int i = 1; i < n-1; ++i){
        if(max(v[i],v[i+1]) < min){
            min = max(v[i],v[i+1]);
        }
    }
    return min-1;
}

int main(){
    int t;
    cin >> t;
    vector <int> results;
    for(int i = 0;i<t;++i){
        int n;
        cin >> n;
        vector <int> v;
        for (int j =0;j<n;++j){
            int a;
            cin >> a;
            v.push_back(a);
        }
        results.push_back(solve(n,v));
    }
    for (int i = 0; i < results.size(); ++i){
        cout << results[i] << endl;
    }
}