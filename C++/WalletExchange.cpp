#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int t;
    vector<string> results;
    cin >> t;
    for(int i = 0;i<t;++i){
        int a,b;
        cin >> a >> b;
        if((a+b) % 2 == 0)results.push_back("Bob");
        else results.push_back("Alice");
    }
    for(int i = 0;i<t;++i){
        cout << results[i] << endl;
    }
}