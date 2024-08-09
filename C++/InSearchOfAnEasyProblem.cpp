#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n;
    cin >> n;
    string result;
    vector<int> a(n);
    for(int i = 0;i < n;++i){
        cin >> a[i];
        if(a[i] == 1){
            result = "HARD";
        }
    }
    if(result == "HARD"){
        cout << "HARD" << endl;
    }else{
        cout << "EASY" << endl;
    }
    return 0;
}