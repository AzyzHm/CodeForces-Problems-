#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> v;
    for(int i = 0; i < n; ++i){
        int x;
        cin >> x;
        v.push_back(x);
    }
    int police  = 0;
    int crimes = 0;
    for(int j = 0;j < n; ++j){
        if(v[j] == -1){
            if(police == 0){
                crimes++;
            }else{
                police--;
            }
        }else{
            police += v[j];
        }
    }
    cout << crimes << endl;
}