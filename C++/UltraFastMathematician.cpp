#include <iostream>

using namespace std;

int main(){
    string s,t;
    cin >> s >> t;
    string result = "";
    for(int i = 0; i < s.size(); i++){
        if(s[i] == t[i]){
            result += "0";
        }else{
            result += "1";
        }
    }
    cout << result << endl;
}