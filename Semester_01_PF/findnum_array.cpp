#include <iostream>

using namespace std;

main()

{

int n[3] = {34, 98, 45}, findNum;

cout << "Please Enter the Number: ";

cin >> findNum;

for (int idx = 0; idx < 3; idx = idx + 1){

if (n[idx] == findNum){

cout << "The number is present in the array" << endl;

}

else{

cout << "The number is not present in the array" << endl;

}

}

}