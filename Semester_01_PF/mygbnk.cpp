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
long long stored_cnic = 0; // Use long long for large CNIC numbers
int stored_password = 0;
int balance = 0;
bool account_exists = false; // Flag to check if account is created

void login() {
    long long cnic;
    int password;
    cout << "Enter your CNIC number: \n";
    cin >> cnic;
    cout << "Enter your password: \n";
    cin >> password;

    // Check if account exists and credentials match
    if (account_exists && cnic == stored_cnic && password == stored_password) {
        cout << "Login successful!\n";
        cout << "Welcome, " << fname << "!\n";
        fchoices();
    } else {
        cout << "Account does not exist or incorrect credentials.\n";
        cout << "Please create a new account or try again.\n";
    }
}

void createAcc() {
    // If account already exists, inform user
    if (account_exists) {
        cout << "An account already exists. Please login.\n";
        login();
        return;
    }

    cout << "Enter your first name: \n";
    cin >> fname;
    cout << "Enter your last name: \n";
    cin >> lname;
    cout << "Enter your father name: \n";
    cin >> father;
    cout << "Enter your CNIC number: \n";
    cin >> stored_cnic;

    int passw, passwcon;
    cout << "Make your password for security purpose: \n";
    cin >> passw;
    cout << "Confirm your password: \n";
    cin >> passwcon;

    if (passw == passwcon) {
        stored_password = passw;
        balance = 2000; // Initial reward
        account_exists = true; // Mark account as created
        cout << "Congratulations! Your account created successfully and you have got the new account reward amount of PKR 2000.\n";
        cout << "Your initial balance is: 2000\n";
        cout << "Returning to main menu to login.\n";
    } else {
        cout << "Passwords do not match. Account creation failed.\n";
        cout << "Please try creating the account again.\n";
        createAcc(); // Retry account creation
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
    bool continue_menu = true; // Flag to control menu loop
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
            continue_menu = false; // Exit the menu
        } else {
            cout << "Invalid choice. Please select a number between 1 and 5.\n";
        }
    }
}

int main() {
    bool continue_program = true; // Flag to control main loop
    while (continue_program) {
        cout << "                                     ******************************************************************************\n";
        cout << "                                                       WELCOME TO BANK MANAGEMENT SYSTEM \n";
        cout << "                                     ******************************************************************************\n";
        cout << endl;
        cout << "1. LOGIN TO YOUR ACCOUNT \n";
        cout << "2. CREATE A NEW ACCOUNT \n";
        cout << "3. EXIT PROGRAM \n";
        int choice;
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1) {
            login();
        } else if (choice == 2) {
            createAcc();
        } else if (choice == 3) {
            cout << "Thank you for using the Bank Management System. Goodbye!\n";
            continue_program = false; // Exit the program
        } else {
            cout << "Invalid choice. Please try again.\n";
        }
    }

    return 0;
}