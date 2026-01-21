#include <iostream>
#include <string>
using namespace std;

// Function prototypes
void login();
void createAcc();
void fchoices();
void deposit();
void withdraw();
void accountDetails();
void checkBalance();

// Global variables for single account
string fname, mname, lname, father;
long long stored_cnic = 0;
int stored_password = 0;
int balance = 0;
bool account_exists = false;

void createAcc() {
    if (account_exists) {
        cout << "An account already exists. Please login.\n";
        login();
        return;
    }

    cout << "Enter your first name: \n";
    cin >> fname;
    cin >> ws; // Consume newline
    cout << "Enter your last name: \n";
    cin >> lname;
    cin >> ws; // Consume newline
    cout << "Enter your father name: \n";
    cin >> father;
    cin >> ws; // Consume newline

    cout << "Enter your CNIC number: \n";
    cin >> ws; // Consume any whitespace
    cin >> stored_cnic;

    int passw, passwcon;
    cout << "Make your password for security purpose: \n";
    cin >> ws; // Consume any whitespace
    cin >> passw;
    cout << "Confirm your password: \n";
    cin >> ws; // Consume any whitespace
    cin >> passwcon;

    if (passw == passwcon) {
        stored_password = passw;
        balance = 2000;
        account_exists = true;
        cout << "Congratulations! Your account created successfully and you have got the new account reward amount of PKR 2000.\n";
        cout << "Your initial balance is: 2000\n";
        cout << "Returning to main menu to login.\n";
    } else {
        cout << "Passwords do not match. Please try entering the password again.\n";
        cout << "Make your password for security purpose: \n";
        cin >> ws; // Consume any whitespace
        cin >> passw;
        cout << "Confirm your password: \n";
        cin >> ws; // Consume any whitespace
        cin >> passwcon;
        if (passw == passwcon) {
            stored_password = passw;
            balance = 2000;
            account_exists = true;
            cout << "Congratulations! Your account created successfully and you have got the new account reward amount of PKR 2000.\n";
            cout << "Your initial balance is: 2000\n";
            cout << "Returning to main menu to login.\n";
        } else {
            cout << "Passwords do not match again. Account creation failed.\n";
            cout << "Returning to main menu.\n";
        }
    }
}

void login() {
    long long cnic;
    int password;
    cout << "Enter your CNIC number: \n";
    cin >> cnic;
    cout << "Enter your password: \n";
    cin >> password;

    if (account_exists && cnic == stored_cnic && password == stored_password) {
        cout << "Login successful!\n";
        cout << "Welcome, " << fname << "!\n";
        fchoices();
    } else {
        cout << "Account does not exist or incorrect credentials.\n";
        cout << "Please create a new account or try again.\n";
    }
}

void deposit() {
    int amount;
    cout << "Enter amount to deposit: \n";
    cin >> amount;
    if (amount > 0) {
        balance = balance + amount;
        cout << "Deposit successful! New balance: " << balance << " PKR\n";
    } else {
        cout << "Invalid amount. Please enter a positive value.\n";
    }
}

void withdraw() {
    int amount;
    cout << "Enter amount to withdraw: \n";
    cin >> amount;
    if (amount > 0) {
        if (amount <= balance) {
            balance = balance - amount;
            cout << "Withdrawal successful! New balance: " << balance << " PKR\n";
        } else {
            cout << "Insufficient balance.\n";
        }
    } else {
        cout << "Invalid amount. Please enter a positive value.\n";
    }
}

void accountDetails() {
    cout << "Account Details:\n";
    cout << "First Name: " << fname << "\n";
    cout << "Last Name: " << lname << "\n";
    cout << "Father's Name: " << father << "\n";
    cout << "CNIC Number: " << stored_cnic << "\n";
}

void checkBalance() {
    cout << "Current Balance: " << balance << " PKR\n";
}

void fchoices() {
    int choice;
    bool continue_menu = true;
    while (continue_menu) {
        cout << "\n1. DEPOSIT\n";
        cout << "2. WITHDRAW\n";
        cout << "3. ACCOUNT DETAILS\n";
        cout << "4. CHECK BALANCE\n";
        cout << "5. EXIT\n";
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1) {
            deposit();
        } else if (choice == 2) {
            withdraw();
        } else if (choice == 3) {
            accountDetails();
        } else if (choice == 4) {
            checkBalance();
        } else if (choice == 5) {
            cout << "Returning to main menu.\n";
            continue_menu = false;
        } else {
            cout << "Invalid choice. Please select a number between 1 and 5.\n";
        }
    }
}

int main() {
    bool continue_program = true;
    while (continue_program) {
        cout << "                                     ******************************************************************************\n";
        cout << "                                                       WELCOME TO BANK MANAGEMENT SYSTEM \n";
        cout << "                                     ******************************************************************************\n";
        cout << endl;
        cout << "1. LOGIN TO YOUR ACCOUNT \n";
        cout << "2. CREATE A NEW ACCOUNT \n";
        cout << "3. EXIT PROGRAM \n";
        cout << "Enter your choice: ";
        int choice;
        cin >> ws; // Consume any leftover whitespace
        cin >> choice;

        if (choice == 1) {
            login();
        } else if (choice == 2) {
            createAcc();
        } else if (choice == 3) {
            cout<< "Thank you for using the Bank Management System. Goodbye!\n";
            continue_program = false;
        } else {
            cout << "Invalid choice. Please try again.\n";
        }
    }

    return 0;
}