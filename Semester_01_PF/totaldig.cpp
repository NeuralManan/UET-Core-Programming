#include<iostream>
using namespace std;

void totaldigits();

int main(){

totaldigits();

}

void totaldigits(){
int num, result;
int count = 0;
cout<<" enter a number : \n";
cin>>num;

while(num !=0){
num = num/10;
count = count + 1;
result = count;
}
cout<<" the total digits are : "<< result <<endl;

}


