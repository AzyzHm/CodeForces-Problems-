#include <iostream>
#include <vector>

using namespace std;

int main(){
    int t;
    cin >> t;
    vector<char> results;
    for(int i = 0; i < t; i++){
        int a,b,c;
        cin >> a >> b >> c;
        if (a + b == c) {
            results.push_back('+');
        } else {
            results.push_back('-');
        }
}
    for(char result:results){
        cout << result << endl;
    }
}