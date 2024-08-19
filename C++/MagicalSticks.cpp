#include <iostream>
#include <vector>

using namespace std;

int main(){
    short t;
    cin >> t;
    vector<int> results;
    while(t--){
        int n;
        cin >> n;
        if(n%2==0){
            results.push_back(n/2);
        }else{
            results.push_back(n/2+1);
        }
    }
    for(int i=0; i<results.size(); i++){
        cout << results[i] << endl;
    }
    return 0;
}