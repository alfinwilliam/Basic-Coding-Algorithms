#include <iostream>
using namespace std;

int main(){
    int limit,i=0,a=0,b=1,c;
    cout<<"Enter the limit : ";
    cin>>limit;
    if(limit<0){ cout<<"invalid limit! "; exit(0); }
    while(i<limit){
        if(i==0){
            cout<<a; cout<<"\n";
        }
        else
        if(i==1){
            cout<<b; cout<<"\n";
        }
        else{
            c = a + b;
        cout<<c; cout<<"\n";
        a = b;
        b = c; }
        i++;
    }
}