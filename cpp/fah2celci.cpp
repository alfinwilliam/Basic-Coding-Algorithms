#include <iostream>
using namespace std;

int main(){
    float v,a;
    cout<<"For Fahrenheit to Celcius : 1\nFor Clecius to Fahrenheit : 2\n";
    cin>>a;
    if(a!=1 && a!=2){
        cout<<"Invalid option\n";
        exit(0);
    }
    cout<<"Enter value\n";
    cin>>v;
    cout<<( a==1? ((v - 32.0) * 5.0 / 9.0) : ((v * 9.0) / 5.0 + 32))<<endl;
    }