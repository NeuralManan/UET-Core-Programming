#include<iostream>
#include<fstream>
using namespace std; 
int main() {
    string task;
        ifstream in("taskresult.txt");
        getline(in, task);
        cout<<task;
        return 0;
}