#include<iostream>
using namespace std;

void parity();

int main(){
parity();

}

void parity(){
int num, num1, num2, num3, num4, prod;
float prodp, nump;
cout<<"enter a three dig number :\n";
cin>>num;
nump = num%2;

num1= num%10;
num2= num/10;
num3= num2%10;
num4= num/100;

prod = num1*num3*num4;
prodp = prod%2;

if(prodp == nump){
cout<<"true";
//return true;
}
else
{cout<<"false";
//return false;
}
}
