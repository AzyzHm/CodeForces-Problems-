#include <iostream>
#include <vector>

using namespace std;

int solve(int a,int b){
    if(a>=b+1){
        return b*2 + 1;
    }
    else if(a == b){
        return a+b-1;
    }else{
        return a*2 - 1;
    }
}
int main(){
    int t;
    cin >> t;
    vector <int> results;
    for(int i = 0;i<t;++i){
        int b,c,h;
        cin >> b >> c >> h;
        results.push_back(solve(b,c+h));
    }
    for (int i = 0; i < results.size(); ++i){
        cout << results[i] << endl;
    }
}