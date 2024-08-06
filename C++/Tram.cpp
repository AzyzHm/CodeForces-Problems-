#include <iostream>
#include <vector>

using namespace std;

int solve(vector<int> a,int n){
    int maximum = 0;
    int current = 0;
    for(int i = 0;i < n*2;i+=2){
        current = current + a[i+1] - a[i];
        maximum = max(maximum,current);
    }
    return maximum;
}

int main(){
    int n;
    cin >> n;
    vector<int> results;
    vector<int> a;
    for(int i = 0;i < n;++i){
        int x,y;
        cin >> x >> y;
        a.push_back(x);
        a.push_back(y);
        }
    results.push_back(solve(a,n));
    for(int i:results){
        cout << i << endl;
    }
}