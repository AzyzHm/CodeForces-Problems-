#include <iostream>
#include <vector>

using namespace std;

int main(){
    int t;
    cin >> t;
    vector<int> results;
    for(int i = 0;i < t;++i){
        int h,m;
        cin >> h >> m;
        results.push_back((23-h)*60 + (60-m));
    }
    for(int res:results){
        cout<<res<<endl;
    }
}