#include <iostream>
using namespace std;

const int WITHDRAW_LIMIT = 300000;
const int MAX_ACCOUNTS = 10; 
int Acc_num[MAX_ACCOUNTS] = {12345678, 98765432};  
string Acc_name[MAX_ACCOUNTS] = {"ali", "Wahab"};  
float Acc_balance[MAX_ACCOUNTS] = {100000, 200000};  
int Acc_password[MAX_ACCOUNTS] = {1234, 5678}; 
int accountCount = 2; 
string Name, Lastname;

int findAccount(double cnic) {
    for (int i = 0; i < accountCount; i++) { 
        if (Acc_num[i] == cnic)
            return i;
    }
    return -1;
}

void accountcreation() {
    if (accountCount >= MAX_ACCOUNTS) {  
        cout << "Cannot create more accounts. Maximum limit reached." << endl;
        return;
    }

    cout << "Enter your FirstName: ";
    cin >> Name;
    cout << "Enter your LastName: ";
    cin >> Lastname;

    double Phone_number, cnic;
    
    // Keep asking for CNIC until a unique one is entered
    while (true) {
        cout << "Enter your cnic: ";
        cin >> cnic;
        
        if (findAccount(cnic) == -1) {
            break;  // CNIC is unique, exit the loop
        }
        cout << "Account with this CNIC already exists! Please enter a different CNIC." << endl;
    }
    
    cout << "enter your Phone number: ";
    cin >> Phone_number;

    int Password, Confirm_Password;

    while (true) {
        cout << "enter your Password (4 digits): ";
        cin >> Password;
        cout << "Confirm Password: ";
        cin >> Confirm_Password;
        if (Password >= 1000 && Password <= 9999) {
            if (Password == Confirm_Password) {
                
                Acc_num[accountCount] = cnic;
                Acc_name[accountCount] = Name + " " + Lastname;
                Acc_balance[accountCount] = 0;
                Acc_password[accountCount] = Password;
                accountCount++;  
                
                cout << "Password Confirmed!" << endl;
                cout << "Your account is created successfully!" << endl;
                cout << "Your account number: " << cnic << endl;
                break;
            } else {
                cout << "Passwords do not match!" << endl;
            }
        } else {
            cout << "Invalid password! It must be a 4-digit number." << endl;
        }
    }
}

void mainMenu(float &balance, float &CurrentBalance) {
    int amount;  
    while (true) {
        int option;
        cout << "\n=== Main Menu ===" << endl;
        cout << "1. Deposit Money" << endl;
        cout << "2. Withdraw Money" << endl;
        cout << "3. Check Balance" << endl;
        cout << "4. Exit to Welcome Menu" << endl;
        cout << "Enter your option (1-4): ";
        cin >> option;

        if (option == 1) {
            cout << "Enter amount to deposit: ";
            cin >> amount;
            if (amount > 0) {
                balance += amount;
                cout << "Deposit successful!" << endl;
                CurrentBalance = balance;
                cout << "Remaining Balance: " << CurrentBalance << endl;
            } else {
                cout << "Invalid amount!" << endl;
            }
        } else if (option == 2) {
            cout << "Enter amount to withdraw: ";
            cin >> amount;
            
            if (amount > 0 && amount <= WITHDRAW_LIMIT) {
                if (amount <= balance) {
                    balance -= amount;
                    cout << "Withdrawal successful!" << endl;
                    CurrentBalance = balance;
                    cout << "Remaining Balance: " << CurrentBalance << endl;
                } else {
                    cout << "Not enough balance!" << endl;
                }
            } else {
                cout << "Amount exceeds withdrawal limit of " << WITHDRAW_LIMIT << "!" << endl;
            }
        } else if (option == 3) {
            cout << "Current Balance: " << CurrentBalance << endl;
        } else if (option == 4) {
            cout << "Returning to Welcome Menu..." << endl;
            break;
        } else {
            cout << "Invalid choice! Please enter 1-4." << endl;
        }
    }
}

int main() {
    cout << "*" << endl;
    cout << "           Welcome to the Bank of UET " << endl;
    cout << "*" << endl;

    int initialChoice;
    float balance = 0.0;
    float CurrentBalance = 0.0;
    int index = -1;

    while (true) {
        cout << "\n=== Welcome Menu ===" << endl;
        cout << "1. Create Account" << endl;
        cout << "2. Login" << endl;
        cout << "3. Exit" << endl;
        cout << "Enter your choice (1-3): ";
        cin >> initialChoice;

        if (initialChoice == 1) {
            accountcreation();
        } else if (initialChoice == 2) {
            double cnicInput;
            cout << "Enter your CNIC to login: ";
            cin >> cnicInput;

            index = findAccount(cnicInput);

            if (index != -1) {
                int enteredPassword;
                cout << "Enter your password: ";
                cin >> enteredPassword;

                if (enteredPassword != Acc_password[index]) {
                    cout << "Incorrect password! Access denied." << endl;
                    continue;
                }

                cout << "\nWelcome Back " << Acc_name[index] << endl;
                cout << "Your account number: " << Acc_num[index] << endl;
                cout << "Your current balance: " << Acc_balance[index] << endl;

                balance = Acc_balance[index];
                CurrentBalance = balance;
                
                mainMenu(balance, CurrentBalance);
                
                if (index != -1) {
                    Acc_balance[index] = balance;
                }
            } else {
                cout << "Account not found! Please create an account first." << endl;
            }
        } else if (initialChoice == 3) {
            cout << "Thank you for visiting Bank of UET. Goodbye!" << endl;
            break;
        } else {
            cout << "Invalid choice! Please enter 1-3." << endl;
        }
    }

    return 0;
}