#include<iostream>
#include<vector>

using namespace std;

string solve(int n){
    int count = 0;
    string res = "";
    int temp = n;
    for(int i = 10000; i >= 1; i /= 10){
        if(temp / i != 0){
            count++;
        }
        temp %= i;
    }
    res += to_string(count) + "\n";
    int i = 10000;
    while(n){
        if(n / i != 0){
            res += to_string(n / i * i) + " ";
        }
        n %= i;
        i /= 10;
    }
    res += "\n";
    return res;
}
int main() {
    int t;
    cin >> t;
    vector<string> res;
    while(t--){
        int n;
        cin >> n;
        res.push_back(solve(n));
    }
    for(auto i : res){
        cout << i;
    }
    return 0;
}