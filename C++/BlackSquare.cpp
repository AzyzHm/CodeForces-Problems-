#include <iostream>
#include <vector>

using namespace std;

int main(){
    short a,b,c,d;
    cin >> a >> b >> c >> d;
    vector<short> v;
    v.push_back(a);
    v.push_back(b);
    v.push_back(c);
    v.push_back(d);
    string s;
    cin >> s;
    int sum = 0;
    for(int i = 0; i < s.size(); i++) {
        short index = s[i] - '0' - 1;
        sum += v[index];
    }
    cout << sum << endl;
}