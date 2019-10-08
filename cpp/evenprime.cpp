#include <iostream>
using namespace std;

int main()
{
    int a;
    cout<<"enter a number";
    cin>>a;
    cout<<(a%2==0? "even" : "odd") <<endl;
    for(int i=2; i<=a/2; ++i){
        if(a%i == 0)
        {   cout<<"not prime"; 
            break;
        }
        else
        {   cout<<"prime"; 
            break; 
        }
    }
}