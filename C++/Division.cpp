#include <iostream>
#include <vector>

using namespace std;

int main(){
    int t;
    cin >> t;
    vector<string> results;
    for(int i = 0; i < t; i++){
        int n;
        cin >> n;
        if (n >= 1900) {
            results.push_back("Division 1");
        } else if (n >= 1600) {
            results.push_back("Division 2");
        } else if (n >= 1400) {
            results.push_back("Division 3");
        } else {
            results.push_back("Division 4");
        }
        }
    for(string result:results){
        cout << result << endl;
    }
}
