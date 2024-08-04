#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solve(int n,int k,vector<int> arr){
    int count = 0;
    for(int j = 0;j < k;++j)
    {
        if(arr[j] > k)
        {
            count++;
        }
    }
    return count;
}
int main() {
    int t;
    cin >> t;
    vector<int> results;
    for(int i = 0;i < t;++i)
    {
        int n,k;
        cin >> n >> k;
        vector<int> arr;
        for(int j = 0;j < n;++j)
        {
            int a;
            cin >> a;
            arr.push_back(a);
        }
        results.push_back(solve(n,k,arr));
    }
    for(int i = 0;i < results.size();++i)
    {
        cout << results[i] << endl;
    }
}