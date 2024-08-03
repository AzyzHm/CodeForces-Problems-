#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool find_key(vector<char> v,char c){
    for(int i = 0;i < v.size();++i){
        if (v[i] == c)return true;
    }
    return false;
}

string solve(string s){
    vector<char> v(3);
    for(int i = 0;i < s.size();++i){
        if(s[i] == 'R' || s[i] == 'G' || s[i] == 'B'){
            if(!find_key(v,tolower(s[i])))return "No";
        }else v.push_back(s[i]);
    }
    return "Yes";
}

int main(){
    int t;
    cin >> t;
    vector <string> results;
    for(int i = 0;i < t;++i){
        string s;
        cin >> s;
        results.push_back(solve(s));
    }
    for(int j = 0;j < results.size();++j){
        cout << results[j] << endl;
    }
}