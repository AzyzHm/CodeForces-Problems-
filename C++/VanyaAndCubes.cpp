#include <iostream>
#include <vector>

using namespace std;

int sum(int n){
    if(n == 1){
        return 1;
    }else{
        return n + sum(n - 1);
    }
}

int main(){
    int n;
    cin >> n;
    int i = 1;
    while(sum(i) <= n){
        n -= sum(i);
        i++;
    }
    cout<<i-1<<endl;
}