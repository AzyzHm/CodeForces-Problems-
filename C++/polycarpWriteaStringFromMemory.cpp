#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool inside(char c,vector<char> v){
    for(int i = 0;i < v.size();++i){
        if(c == v[i]){
            return true;
        }
    }
    return false;
}

int solve(string s){
    vector <char> v;
    int n = s.size();
    int count_days = 0;
    for(int i = 0;i < n;i++){
        if(!inside(s[i],v))v.push_back(s[i]);
        if(v.size() == 4){
            count_days++;
            v.clear();
            v.push_back(s[i]);
        }
        if(i == n-1){
            count_days++;
            v.clear();
        }
    }
    return count_days;
}

int main(){
    int t;
    cin >> t;
    vector<int> results;
    for(int i = 0;i < t;++i){
        string s;
        cin >> s;
        results.push_back(solve(s));
    }
    for(int i = 0;i < results.size();++i){
        cout << results[i] << endl;
    }
}