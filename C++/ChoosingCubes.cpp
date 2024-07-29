#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

string solve(int n,int f,int k,vector<int> cubes){
    int favourite = cubes[f-1];
    int count = 0;
    sort(cubes.begin(),cubes.end(),[](int a,int b){return a>b;});
    for(int i = 0;i<n;++i){
        if(cubes[i] == favourite)count++;
    }
    int new_count = 0;
    for (int i = k; i < n; i++) {
        if (cubes[i] == favourite) {
            new_count++;
        }
    }
    if(count == new_count)return "No";
    else if (new_count == 0) return "Yes";
    else return "Maybe";
}

int main(){
    int t;
    vector<string> results;
    cin >> t;
    for(int i = 0;i<t;++i){
        int n,f,k;
        vector<int> cubes;
        cin >> n >> f >> k;
        for(int j = 0;j<n;++j){
            int cube;
            cin >> cube;
            cubes.push_back(cube);
        }
        results.push_back(solve(n,f,k,cubes));
    }
    for(int i = 0;i<t;++i){
        cout << results[i] << endl;
    }
}