#include<iostream>
using namespace std;
int collatz();
int collatz1();
int series;
int main(){
int n;
cout<<"integer n = ";
cin>> n;
if(n%2 == 0){
collatz();
}
else
{ collatz1();
}

}

int collatz(){
int n;
while(n%2 == 0){

series = n--;
if(series%2 == 0){
cout<<series<<", ";
}
}
}

int collatz1(){
int n;

while(n%2 != 0){
int series;
series = n--;
if(series%2 != 0){
int series1;
series1 = (series*3)+1;
cout<<series1<<", ";
}
}
}




