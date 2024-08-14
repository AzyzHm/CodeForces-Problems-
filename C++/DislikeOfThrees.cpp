#include <iostream>
#include <vector>

using namespace std;

int main(){
    short t;
    cin >> t;
    vector<short> tests;
    vector<short> results;
    while(t--){
        short temp;
        cin >> temp;
        tests.push_back(temp);
    }
    short i = 1;
    short number = 1;
    for(short test : tests){
        if(i < test){
            while(i < test){
                number++;
                if(number % 3 == 0 || number % 10 == 3){
                    continue;
                }
                i++;
            }
        }
        else{
            while(i > test){
                number--;
                if(number % 3 == 0 || number % 10 == 3){
                    continue;
                }
                i--;
            }
        }
        results.push_back(number);
    }
    for(short result : results){
        cout << result << endl;
    }
}