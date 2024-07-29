#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int factorial(int n){
    if(n == 0)return 1;
    return n*factorial(n-1);
}
int main(){
        int a,b;
        cin >> a >> b;
        cout << factorial(min(a,b)) << endl;
    
}