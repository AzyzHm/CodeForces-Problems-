// not completed²
#include <iostream>
#include <vector>

using namespace std;
int solve(long n,vector<long> a){
    int count = 0;
    for(int i = 0;i < n;++i){
        for (int j = i+1;j < n;++j){
            if((a[i]%2 == 0 && a[j]%2 != 0) || (a[i]%2 != 0 && a[j]%2 == 0)){
                count++;
                if(a[i]<a[j]){
                    a[i] = a[i] + a[j];
                }
                else{
                    a[j] = a[i] + a[j];
                }
        }
    }
    return count;
}
}

int main(){
    int t;
    cin >> t;
    vector<int> results;
    for(int i = 0;i<t;++i){
        long n;
        cin >> n;
        vector<long> a;
        for(int j = 0;j < n;++j){
            long temp;
            cin >> temp;
            a.push_back(temp);
        }
        results.push_back(solve(n,a));
    }
    for(int i = 0;i < results.size();++i){
        cout << results[i] << endl;
    }
}