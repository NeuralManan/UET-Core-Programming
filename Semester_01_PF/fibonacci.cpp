#include<iostream>
using namespace std;

void generateFibonacci();

int main(){

generateFibonacci();


}

void generateFibonacci(){
int length;
cout<<" enter the length of the Fibonacci series :\n";
cin>>length;
int num, num1, num2;
num1=0;
num2=1;
for(int x=0; x<=length; x++){
num= num1+num2;
cout<<num1<<", ";
num1=num2;
num2=num;
}
}
