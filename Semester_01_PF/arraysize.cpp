#include<iostream>
using namespace std;
int main(){
    int marks[5]={11,12,23,45,67};
    int size = 5; //it is already given but if we don't know the size we can adopt following formula:
   int arraysize=sizeof(marks)/sizeof(int);
    cout<< arraysize;// calculates array size automatically{ sizeof(marks) calculates no. of bytes taken by the array and sizeof(int) cdivided by this means dividing by the bytes of datatype}
}