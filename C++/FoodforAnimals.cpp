#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int t;
    vector<string> results;
    cin >> t;
    for(int i = 0;i<t;++i){
        int a,b,c,x,y;
        cin >> a >> b >> c >> x >> y;
        if(x>a)c-=(x-a);
        if(y>b)c-=(y-b);
        if(c>=0)results.push_back("YES");
        else results.push_back("NO");
    }
    for(int i = 0;i<t;++i){
        cout << results[i] << endl;
    }
}