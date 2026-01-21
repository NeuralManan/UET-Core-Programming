#include<iostream>
using namespace std;
int trnum,dnum1,dnum2;
int main(){

cout<<"Enter number of triangle: ";
cin>>trnum;
int result = 1;
for(int i = trnum; i >= 1; i--){
result *=i;
}
cout<<"Dots in the triangle: "<<result;
}
