#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){
    int t;
    cin >> t;
    vector<string> results;
    for (int i = 0; i < t; i++)
    {
        string s;
        cin >> s;
        int n = s.size();
        if (n % 2 == 0)
        {
            string s1 = s.substr(0, n / 2);
            string s2 = s.substr(n / 2, n / 2);
            if (s1 == s2)
            {
                results.push_back("YES");
            }
            else
            {
                results.push_back("NO");
            }
        }
        else
        {
            results.push_back("NO");
        }
    }
    for(string res:results){
        cout<<res<<endl;
    }
    
}