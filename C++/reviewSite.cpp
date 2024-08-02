#include <iostream>
#include <vector>

using namespace std;

int solve(int n,vector<int> v){
    int upvotes = 0;
    for(int i = 0;i < n;++i){
        if(v[i] == 1 || v[i] == 3){
            upvotes++;
        }
    }
    return upvotes;
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