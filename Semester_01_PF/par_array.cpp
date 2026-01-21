#include <iostream>

using namespace std;

main()

{

string Names[100];

int IDs[100];

float Gpa[100];

int count = 0;

bool takeInput = true;

while (takeInput == true) //For Taking Input

{

cout << "Name: ";

cin >> Names[count];

cout << "Roll Number: ";

cin >> IDs[count];

cout << "GPA: ";

cin >> Gpa[count];

cout << "If you want to enter another record press 1 otherwise 0: ";

cin >> takeInput;

count = count + 1;

}

cout << "Name" << "\t" << "ID" << "\t" << "GPA" << endl;

for (int idx = 0; idx < count; idx = idx + 1) //For Displaying Output

{

cout << Names[idx] << "\t" << IDs[idx] << "\t" << Gpa[idx] << endl;

}

}
