#include <iostream>
#include <string>
using namespace std;

int main() {
 string str;
 cout << "Enter a string: ";
 getline(cin, str);
    
int count = 0;
 while(str[count] != '\0') {
        count++;
 }
 if(count % 2 == 0) {
 cout << "true" << endl;
} else {
 cout << "false" << endl;
}
    return 0;
}