#include <iostream>
#include <vector>

using namespace std;

int main(){
    int t;
    cin >> t;
    vector<string> res;
    while(t--){
        int n;
        cin >> n;
        if(n % 4 != 0){
        res.push_back("NO");
    }
    else{
        string s = "YES\n";
        for(int i = 2; i <= n; i += 2){
        s += to_string(i) + " ";
        }
        for(int i = 1; i < n - 1; i += 2){
        s += to_string(i) + " ";
        }
        s += to_string(n + n / 2 - 1);
        res.push_back(s);
    }
    }
    for(int i = 0; i < res.size(); i++){
        cout << res[i] << endl;
    }
    
}