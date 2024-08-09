#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

bool inside(string s,char c){
    for(int i = 0;i < s.size();++i){
        if(s[i] == c){
            return true;
        }
    }
    return false;
}

int main(){
    int n;
    string s;
    cin >> n;
    cin >> s;

    if (n < 26){
        cout << "NO" << endl;
        return 0;
    }
    
    // Convert the string to lowercase
    transform(s.begin(), s.end(), s.begin(), ::tolower);

    vector<char> a = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
         'p','q','r','s','t','u','v','w','x','y','z'};
    for(int i = 0;i < a.size();++i){
       if(!inside(s,a[i])){
           cout << "NO" << endl;
           return 0;
       }
    }
    cout << "YES" << endl;
    return 0;
}