#include <iostream>
#include <vector>

using namespace std;
int solve(vector<int> a){
    int result = 0;
    for(int i = 0; i < a.size(); i+=2){
        if (a[i+1]<a[i]) {
            result++;
        }
    }
    return result;
}
int main(){
    int t;
    cin >> t;
    vector<int> results;
    for (int i = 0; i < t; ++i) {
        int n;
        cin >> n;
        vector<int> a(n*2);
        for (int j = 0; j < n*2; j+=2) {
            cin >> a[j] >> a[j+1];
        }
        results.push_back(solve(a));
    }
    for (const auto& result : results) {
        cout << result << endl;
    }
}