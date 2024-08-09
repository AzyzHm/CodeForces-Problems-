#include <iostream>
#include <vector>

using namespace std;

int main(){
    int t;
    cin >> t;
    vector<long> results;
    for(int i = 0;i < t;++i){
        long a,b;
        cin >> a >> b;
        if(a % b == 0)results.push_back(0);
        else{
        if(a>=b){
            results.push_back(b - (a % b));
        }else{
            results.push_back(b - a);
        }
        }
    }
    for(long result:results){
        cout << result << endl;
    }
}