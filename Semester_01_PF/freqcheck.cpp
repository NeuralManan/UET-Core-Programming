#include<iostream>
using namespace std;

void freqcheck();
int number, num;

int main(){

cout<<"Enter a number to check a digit's frequency in it: ";
cin>>number;
cout<<"Enter the digit from the number of which frequency is required: ";
cin>>num;

  freqcheck();
}

void freqcheck(){

int sum;

while(number>0){
if(num == number%10){
sum++;
}
number = number/10;
}
cout<<"frequency: "<<sum;

}

