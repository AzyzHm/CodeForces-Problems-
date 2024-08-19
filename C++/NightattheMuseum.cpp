#include <iostream>
#include <string>

using namespace std;

int main(){
    string s;
    cin >> s;
    int result = 0;
    char current = 'a';
    for(int i=0; i<s.size(); i++){
        int diff = abs(s[i]-current);
        if(diff>13){
            diff = 26-diff;
        }
        result += diff;
        current = s[i];
    }
    cout << result << endl;
    return 0;
}