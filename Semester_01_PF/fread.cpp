#include<iostream>
#include<fstream>
using namespace std; 
int main() {
    char str[200] = "The sun dipped below the horizon, painting the sky in fiery hues as the first stars timidly blinked awake.";
    int count = 0;
    for (int i = 0; str[i] != '\0'; i++) {
        count++;
    }
        cout<<endl;
        cout<<endl;

        ofstream out("taskresult.txt");
        out<<str;
    cout << "no of characters in the given string are = " << count; 
        cout<<endl;
        cout<<endl;


    return 0;

}