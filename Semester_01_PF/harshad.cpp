#include<iostream>
using namespace std;
int Harshad();
int main(){

 Harshad();

}

int Harshad(){
int digit, num1, num2, num3, num4;
cout<<"digit "<<endl;
cin>>digit;
num1=digit%10;
num2=digit/10;
num3= num1+num2;
if(digit%num3 == 0){
cout<<"number is Harshad";
}
else{
cout<<"NOT harshad";
}
}

