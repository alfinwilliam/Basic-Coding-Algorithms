#include <iostream>
using namespace std;

int main()
{
    int a,b,c;
    cout<<"Enter three numbers: ";
    cin>>a>>b>>c;
    if( a>b && a>c) {cout<<"the largest number is "<<a; }
    if( b>a && b>c) {cout<<"The largest number is "<<b; }
    if( c>a && c>b) {cout<<"The largest number is "<<c; }
    return 0;
    }