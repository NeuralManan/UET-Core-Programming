#include <iostream>
using namespace std;

int main() {
int n;
cout << "Enter the size of array: ";
cin >> n;
int arr[n];
cout << "Enter " << n << " numbers: ";
for(int i = 0; i < n; i++) {
cin >> arr[i];
}
bool found = false;
for(int i = 0; i < n; i++) {
string num = to_string(arr[i]);
for(char digit : num) {
if(digit == '7') {
found = true;
break; 
}
 }
 if(found) {
break;
 }    
if(found) {
cout << "Boom!" << endl;
} else {
cout << "there is no 7 in the array" << endl;
}
}
}