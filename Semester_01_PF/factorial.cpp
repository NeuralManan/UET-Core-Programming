#include<iostream>
using namespace std;
 int num1, num2, num3, num4;
int main(){
int num;
cout<<"enter number to calculate factorial: ";
cin>>num;
int result= 1;
for(int i=num; i>= 1; i--){

result *=i;
}
cout<<result;
}

