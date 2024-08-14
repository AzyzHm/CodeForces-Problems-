#include <iostream>
#include <vector>

using namespace std;

int main(){
    int t;
    cin >> t;
    vector<int> results;
    while(t--){
        int a,b,c,d;
        cin >> a >> b >> c >> d;
        int num = 0;
        if(a < b) num++;
        if(a < c) num++;
        if(a < d) num++;
        results.push_back(num);
    }
    for(int i = 0; i < results.size(); ++i){
        cout << results[i] << endl;
    }
}