#include <iostream>
#include <vector>
#include <string>

using namespace std;

string lexico_smallest(string a,string b){
    int i = 0;
    int j = a.size() - 1;
    while(i < j){
        if(a[i] == a[j]){
            i++;j--;
        }else {if(a[i]>b[i])return b;
        else return a;}
    }
}

string solver(string s){
    int n = s.size();
    string reversed_s = "";
    for(int i = 0;i < n;i++){
        reversed_s  = s[i] + reversed_s;
    }
    if(lexico_smallest(s,reversed_s) == s)return s;
    else return reversed_s+s;
}
int main(){
    int t;
    cin >> t;
    vector <string> results;
    for(int i = 0;i < t;++i){
        int n;
        cin >> n;
        string s;
        cin >> s;
        results.push_back(solver(s));
    }
    for(int j = 0;j < results.size();++j){
        cout << results[j] << endl;
    }
}