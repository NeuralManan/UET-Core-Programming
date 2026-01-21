#include <iostream>
using namespace std;
int cnic, password;
void login(){

cout<<"Enter your CNIC number: \n";
cin>>cnic;
cout<<"Enter your password: \n";
cin>>password; 
}


void createAcc(){
string fname, lname, mname, father;
cout<<" Enter your first name: \n";
cin>>fname;
cout<<" Enter your middle name: \n";
cin>>mname;
cout<<" Enter your last name: \n";
cin>>lname;
cout<<" Enter your father name: \n";
cin>>father;
int cnic, passw, passwcon, inibalance;
cout<<"Enter your CNIC number: \n";
cin>>cnic;
cout<<"Make your password for security purpose: \n";
cin>>passw;
cout<<" Confirm your password: \n";
cin>>passwcon;
if(passw == passwcon){
cout<<" Congratulations! Your account created successfully and you have got the new account reward amount of PKR 2000.\n";
cout<<" Your initial balance is: 2000\n"; }
cout<<" Enter your further choices to continue.\n";
cout<<endl;
}

void fchoices(){
cout<<" 1. DEPOSIT\n";
cout<<" 2. WITHDRAW\n";
cout<<" 3. ACCOUNT DETAILS\n";
cout<<" 4. CHECK BALANCE\n";
cout<<" 5. EXIT\n";
}

int main(){
cout<<"                                     ******************************************************************************\n";
cout<<"                                                       WELCOME TO BANK MANAGEMENT SYSTEM \n";
cout<<"                                     ******************************************************************************\n";
cout<<endl;
cout<<"1. LOGIN TO YOUR ACCOUNT \n";
cout<<"2. CREATE A NEW ACCOUNT  \n";
int choice;
cout<<" Enter your choice: ";
cin>>choice;
if(choice == 1){
login();
}
else if (cnic== 12345678910 && password == 1234){
 fchoices();
}

else {
       createAcc();
 }
}




