#include <iostream>
#include <vector>

using namespace std;

string solve(long a,long b,long c,long d){
    if(a > b){
        if(d > c)return "No";
        else return "Yes";
    }
    else {if(b > a){
        if(c > d)return "No";
        else return "Yes";
    }}
}

int main(){
    int t;
    cin >> t;
    vector<string> results;
    for(int i = 0;i < t;++i){
        long a,b,c,d;
        cin >> a >> b;
        cin >> c >> d;
        results.push_back(solve(a,b,c,d));
    }
    for(int i = 0;i < results.size();++i){
        cout << results[i] << endl;
    }
}