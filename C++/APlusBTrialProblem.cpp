#include <iostream>
#include <vector>

using namespace std;

int main(){
    int t;
    cin >> t;
    vector<int> results;
    for(int i = 0;i < t;++i){
        int a,b;
        cin >> a >> b;
        results.push_back(a+b);
    }
    for(int i = 0;i < results.size();++i){
        cout << results[i] << endl;
    }
}