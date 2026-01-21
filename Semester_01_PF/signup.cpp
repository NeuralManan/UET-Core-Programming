#include<iostream>
#include<fstream>
#include <string>
using namespace std;
string names;
string passwords;
void data (fstream& dbase);
int main(){
fstream dbase;
dbase.open("dbase.txt", ios::out);
    cout<<"*************** LOGIN PAGE ********************"<<endl;
    data (dbase);
    dbase.close();

    cout<<endl;
    cout<<endl;

    string dataline;
    dbase.open("dbase.txt", ios::in);
while (!dbase.eof()){
    getline(dbase, dataline) ;
     cout << dataline << endl;
}
    dbase.close();


}
void data(fstream& dbase){
    cout<<"Enter your name: ";
    getline(cin, names);
    cout<<"Enter your password: ";
    getline(cin, passwords);
    dbase << "Name: " << names << "\nPassword: " << passwords << endl;
}