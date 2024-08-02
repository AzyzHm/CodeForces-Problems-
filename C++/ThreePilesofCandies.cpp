#include <iostream>
#include <vector>

using namespace std;

long long sum_vector(vector<long long> v){
    long long sum = 0;
    for(int i = 0; i < v.size(); ++i){
        sum += v[i];
    }
    return sum;
}

int main(){
    int t;
    cin >> t;
    vector <long long> results;
    for(int i = 0;i<t;++i){
        long long a,b,c;
        cin >> a >> b >> c;
        vector <long long> v = {a,b,c};
        results.push_back(sum_vector(v)/2);
    }
    for (int i = 0; i < results.size(); ++i){
        cout << results[i] << endl;
    }
}