#include<iostream>
using namespace std;
int num, count=0,j;

int main(){

 cout<<"Enter the number: ";
cin>>num;

for(j=1; j<=num;j++){
if(num%j==0){
count++;
}
}

if(count==2){
cout<<"The number is a  prime number.";
}
else{
cout<<"The number is not a  prime number.";
}
}


