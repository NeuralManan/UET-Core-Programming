#include<iostream>
using namespace std;
int main(){
    int a = 5;
    cout<< *(&a) <<endl;
    int* ptr = &a;
    int**ptr2 = &ptr;
    cout<<*(ptr)<<endl;
    cout<<**(ptr2)<<endl;//value of a
    cout<<**ptr2<<endl;//address of a
    cout<<*ptr;//address of a
}