#include<iostream>
using namespace std;

void tables(int num);

int main(){
int num;
cout <<" ENTER THE NUMBER FOR WHICH THE TABLE IS REQUIRED: \n";
cin >> num;
tables(num);
}


void tables(int num){
int count, ans;
for(int x=1; x<11; x++){
ans = num*x;
cout<< num <<" * " <<x <<" = " << ans <<endl;
}
}
