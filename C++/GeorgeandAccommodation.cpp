#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n;
    cin >> n;
    int count = 0;
    vector<int> p(n),q(n);
    for(int i = 0;i < n;++i){
        int a,b;
        cin >> a >> b;
        p[i] = a;
        q[i] = b;
        if(b-a >= 2){
        count++;
    }
    }
    cout << count << endl;
}