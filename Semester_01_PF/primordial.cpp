#include<iostream>
using namespace std;
int num, count, j, primorial=1;

int main(){
cout<<"Enter the number: ";
cin>>num;

for(int i=1; num>0; i++){
count=0;
for(j=1; j<=i; j++){
if(i%j==0){
count++;
}
}
if(count==2){
primorial*=i;
num--;
}
}

cout<<"The primorial is: "<<primorial;
}