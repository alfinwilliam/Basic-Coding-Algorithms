#include <iostream>
using namespace std;

int main(){
    float v,a;
    cout<<"Fahrenheit to Celcius , 1\nClecius to Fahrenheit , 2";
    cin>>a;
    cout<<"Enter value";
    cin>>v;
    if(a!=1 && a!=2){
        cout<<"Invalid option";
        exit(0);
    }
    cout<<( a==1? ((v - 32.0) * 5.0 / 9.0) : ((v * 9.0) / 5.0 + 32))<<endl;
    }