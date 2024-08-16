#include <iostream>
#include <vector>
#include <algorithm>
#include <cctype>

using namespace std;

int main(){
    int t;
    cin >> t;
    vector<string> res;
    while(t--){
        string s;
        cin >> s;
        transform(s.begin(), s.end(), s.begin(), ::tolower);
        if(s == "yes"){
            res.push_back("Yes");
        } else {
            res.push_back("No");
        }
    }
    for(auto i : res){
        cout << i << endl;
    }
}