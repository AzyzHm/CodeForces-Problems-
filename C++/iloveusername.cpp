#include <iostream>
#include <vector>

using namespace std;

bool amazing_more(vector<short> v,short n){
    for(short i = 0;i < v.size();++i){
        if(v[i] <= n){
            return false;
        }
    }
    return true;
}
bool amazing_less(vector<short> v,short n){
    for(short i = 0;i < v.size();++i){
        if(v[i] >= n){
            return false;
        }
    }
    return true;
}

int main(){
    short n;
    cin >> n;
    vector<short> v;
    for(int i = 0; i < n; ++i){
        short x;
        cin >> x;
        v.push_back(x);
    }
    vector<short> temp;
    temp.push_back(v[0]);
    short count = 0;
    for(short j = 1;j < n;++j){
        if(amazing_more(temp,v[j]) || amazing_less(temp,v[j])) count++;
        temp.push_back(v[j]);
    }
    cout << count << endl;
}