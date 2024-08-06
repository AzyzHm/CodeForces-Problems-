#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n,h;
    cin >> n >> h;
    vector<int> a;
    int width = 0;
    for(int i = 0;i < n;++i){
        int x;
        cin >> x;
        if(x > h){
            width += 2;
        }else{
            width += 1;
        }
    }
    cout << width << endl;
}