#include <iostream>
#include <vector>

using namespace std;

int number_of_good_dice_rolls(int a,int b){
    int count = 0;
    int maxi = max(a,b);
    for(int i = 1;i <= 6;++i){
        if(i >=maxi ){
            count++;
        }
    }
    return count;
}
int main(){
    int a,b;
    cin >> a >> b;
    int num = number_of_good_dice_rolls(a,b);
    switch (num)
    {
    case 1:
        cout<<"1/6"<<endl;
        break;
    case 2:
        cout<<"1/3"<<endl;
        break;
    case 3:
        cout<<"1/2"<<endl;
        break;
    case 4:
        cout<<"2/3"<<endl;
        break;
    case 5:
        cout<<"5/6"<<endl;
        break;
    default:
        cout<<"1/1"<<endl;
        break;
    }
}