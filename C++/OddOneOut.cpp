#include <iostream>
#include <vector>

using namespace std;

int main() {
    int t;
    cin >> t;
    vector<int> v;
    while(t--) {
        int a,b,c;
        cin >> a >> b >> c;
        if(a != b && a != c) {
            v.push_back(a);
        } else if(b != a && b != c) {
            v.push_back(b);
        } else {
            v.push_back(c);
        }
    }
    for(int i = 0; i < v.size(); i++) {
        cout << v[i] << endl;
    }
    return 0;
}