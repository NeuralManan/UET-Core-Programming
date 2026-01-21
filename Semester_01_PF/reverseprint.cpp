#include<iostream>
using namespace std;
int main(){
int number, num1, num2, num3, num4, num5, num6, num7, num8, num9, num10;
cout<<"Enter a five digit number: ";
cin>> number;
num1 = number%10;
num2 = number/10;
num3 = num2%10;
num4 = num2/10;
num5 = num4%10;
num6 = num4/10;
num7 = num6%10;
num8 = num6/10;
num9 = num8%10;
num10 = num8/10;
cout<<num1<<num3<<num5<<num7<<num9;
}
