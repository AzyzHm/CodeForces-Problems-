#include <iostream>
#include <vector>

using namespace std;

int main(){
    short t;
    cin >> t;
    vector<int> results;
    while(t--){
        int n;
        cin >> n;
        vector<short> a;
        short max = 0;
        short current = 0;
        for(int i=0; i<n; i++){
            short temp;
            cin >> temp;
            a.push_back(temp);
            
            if(i == 0){
                if(temp == 0)current++;
            }else{
                if(temp == 0){
                    if(a[i-1] == 1){
                        max = current>max?current:max;
                        current = 1;
                    }else{
                        current++;
                    }
            }
        }
    }
    max = current>max?current:max;
    results.push_back(max);
    }
    for(int i=0; i<results.size(); i++){
        cout << results[i] << endl;
    }
    return 0;
}