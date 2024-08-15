#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    int n;
    cin >> n;
    double sum = 0;
    for(int i = 0;i < n;++i){
        int x;
        cin >> x;
        sum += x;
    }
    double res = sum / (double)n;
    cout << fixed << setprecision(12) << res << endl;

}