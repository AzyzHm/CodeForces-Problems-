#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int t;
    cin >> t;
    vector<int> results;
    for(int i;i<t;++i){
        int n;
        cin >> n;
        if(n % 3 == 0)results.push_back(n/3);
        else{
            if(n == 1 || n == 4) results.push_back(2);
            else if((n - n/3)%2 == 0) results.push_back(n/3 + (n%3)/2);
            else results.push_back(n/3 + (n%3)/2 + 1);
        }
    }
    for(int i = 0;i<t;++i){
        cout << results[i] << endl;
    }
}