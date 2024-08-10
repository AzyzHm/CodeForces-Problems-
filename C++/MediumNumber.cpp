#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int t;
    cin >> t;
    vector<int> results;
        for(int i = 0; i < t; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        
        int minimum = min({a, b, c});
        int maximum = max({a, b, c});
        
        if(a != minimum && a != maximum) {
            results.push_back(a);
        } else if(b != minimum && b != maximum) {
            results.push_back(b);
        } else {
            results.push_back(c);
        }
    }
    for(int result:results){
        cout << result << endl;
    }
}