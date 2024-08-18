#include <iostream>
#include <vector>

using namespace std;

int main(){
    int t;
    cin >> t;
    vector<string> v;
    while(t--){
        short a,b,c;
        cin >> a >> b >> c;
        if(a + b >= 10) {
            v.push_back("YES");
        } else if(b + c >= 10) {
            v.push_back("YES");
        } else if(a + c >= 10) {
            v.push_back("YES");
        } else {
            v.push_back("NO");
        }
    }
    for(int i = 0; i < v.size(); i++) {
        cout << v[i] << endl;
    }
}