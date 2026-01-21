#include<iostream>
using namespace std;



int main(){
    int arr[11];
    int even[11], odd[11];
    int evenCount = 0;
    int oddCount = 0;
    cout<<"Enter 11 integers:"<<endl;
    for(int i = 0; i < 11; i++){
    cin>>arr[i];
    }
    for(int i = 0; i < 11; i++){
        if(arr[i] % 2 == 0){
    even[evenCount] = arr[i];
    evenCount++;
        } else {
         odd[oddCount] = arr[i];
            oddCount++;
        }
    }
    cout<<"Original Array: ";
    for(int i = 0; i < 11; i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    cout<<"Even Array: ";
    for(int i = 0; i < evenCount; i++){
        cout<<even[i]<<",";
    }
    cout<<endl;
    cout<<"Odd Array: ";
    for(int i = 0; i < oddCount; i++){
        cout<<odd[i]<<",";
    }
    cout<<endl;
    return 0;
}