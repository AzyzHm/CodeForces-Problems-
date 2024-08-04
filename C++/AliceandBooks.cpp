#include <iostream>
#include <vector>

using namespace std;

int solve(int n,vector<int> arr){
    // the last book in the pile is guaranteed to be the one with the highest number in the second pile
    int max_pages_second_pile = arr[n-1];
    // we need to find the book with maximum pages in the first pile
    int max_pages_first_pile = 0;
    for(int i = 0;i < n-1;++i){
        if(arr[i] > max_pages_first_pile){
            max_pages_first_pile = arr[i];
        }
    }
    return max_pages_first_pile + max_pages_second_pile;
}

int main(){
    int t;
    cin >> t;
    vector<int> results;
    for(int i = 0;i < t;++i){
        int n;
        cin >> n;
        vector<int> arr;
        for(int j = 0;j < n;++j){
            int a;
            cin >> a;
            arr.push_back(a);
        }
        results.push_back(solve(n,arr));
    }
    for(int i = 0;i < results.size();++i){
        cout << results[i] << endl;
    }
}