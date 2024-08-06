#include <iostream>
#include <vector>

using namespace std;

string solve(vector<long> a,long s,long m){
    long maximum = a[0];
    for(int i = 1;i < a.size();i += 2){
        if(i == a.size()-1){
            maximum = max(maximum,m-a[i]);
            break;
        }
        maximum = max(maximum,a[i+1]-a[i]);
    }
    if(maximum >= s){
        return "Yes";
    }else return "No";
    
}

int main(){
    int t;
    cin >> t;
    vector<string> results;
    for(int i = 0;i < t;++i){
        long n,s,m;
        cin >> n >> s >> m;
        vector<long> a;
        for(int j = 0;j < n;++j){
            long x,y;
            cin >> x >> y;
            a.push_back(x);
            a.push_back(y);
        }
        results.push_back(solve(a,s,m));
    }
    for(string result : results){
        cout << result << endl;
    }

}