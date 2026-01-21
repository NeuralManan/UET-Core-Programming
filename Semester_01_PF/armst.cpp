#include<iostream>
using namespace std;
int main(){
int number, num1, num2, num3, num4, num5, num6, num7, num8, num9;
cout<<" enter a three digit number: ";
cin>>number;
num1 = number%10;
num2 = number/10;
num3 = num2%10;
num4 = num2/10;
num5 = num4%10;
num6 = num1*num1*num1;
num7 = num3*num3*num3;
num8 = num5*num5*num5;
num9 = num6+num7+num8;
if(number==num9){
cout<<"The number is Armstrong.";
}
else{
cout<<" number is not an Armstrong number.";
}
}
