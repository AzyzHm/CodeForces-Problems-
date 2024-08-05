#include <iostream>
#include <vector>

using namespace std;

int main(){
    int t;
    cin >> t;
    vector<string> results;
    for(int i = 0;i<t;++i){
        string s;
        cin >> s;
        if(s[0] == 'a' || s[1] == 'b' || s[2] == 'c'){
            results.push_back("YES");
        }
        else{
            results.push_back("NO");
        }
    }
    for(int i = 0;i < results.size();++i){
        cout << results[i] << endl;
    }
}