#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

string solve(int n,int sum,vector<int> a){
    if(sum % 2 == 0){
        sort(a.begin(),a.end());
        int sum1 = 0;
        int sum2 = 0;
        for(int i = n-1;i >= 0;--i){
            if(sum1 <= sum2){
                sum1 += a[i];
            }
            else{
                sum2 += a[i];
            }
        }
        if(sum1 == sum2){
            return "Yes";
        }
        else{
            return "No";
        }
    }
    else{
        return "No";
    }
}

int main(){
    int t;
    cin >> t;
    vector<string> results;
    for(int i = 0;i < t;++i){
        int n;
        cin >> n;
        int sum = 0;
        vector<int> a;
        for(int j = 0;j < n;++j){
            int x;
            cin >> x;
            a.push_back(x);
            sum += x;
        }
        results.push_back(solve(n,sum,a));
    } 
    for(string res:results){
        cout<<res<<endl;
    }  
}