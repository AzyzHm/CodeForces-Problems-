#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){
    int t;
    cin >> t;
    vector<string> results;
    for(int i = 0;i < t;++i){
        string n;
        cin >> n;
        if(n.size() < 3)results.push_back("No");
        else{
        string number = n.substr(0,2);
        if(number != "10")results.push_back("No");
        else{
            string expo = n.substr(2);
            if(expo.size() == 1 && (expo == "0" || expo == "1"))results.push_back("No");
            else{
                if(expo[0] == '0')results.push_back("No");
                else results.push_back("Yes");
            }
        }
    }
    }
    for(auto i : results)cout << i << endl;
}