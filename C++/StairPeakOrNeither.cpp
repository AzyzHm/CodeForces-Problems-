#include <iostream>
#include <vector>

using namespace std;

int main(){
    short t;
    cin >> t;
    vector<string> res;
    while(t--){
        short a,b,c;
        cin>>a>>b>>c;
        if(b > a && b > c){
            res.push_back("PEAK");
            continue;
        }
        if(b > a && b < c){
            res.push_back("STAIR");
            continue;
        }
        else{
            res.push_back("NONE");
            continue;
        }
}
    for(auto i: res){
        cout<<i<<endl;
    }
    return 0;
}