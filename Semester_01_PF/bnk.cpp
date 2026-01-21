#include <iostream>
#include <string>
using namespace std;

const int WITHDRAW_LIMIT = 300000;

int Acc_num[10] = {12345678, 98765432};
string Acc_name[10] = {"ali", "Wahab"};
float Acc_balance[10] = {100000, 200000};
int Acc_password[10] = {1234, 5678};
int totalAccounts = 2;
string Name, Surname;

int findAccount(double cnic) {
    for (int i = 0; i < totalAccounts; i++) {
        if (Acc_num[i] == cnic) {
            return i;
        }
    }
    return -1;
}

bool login(double cnic) {
    int index = findAccount(cnic);
    if (index == -1) {
        cout << "Account not found! Please create an account or re-enter correct credentials." << endl;
        return false;
    }
    int password;
    cout << "Enter your 4-digit password: ";
    cin >> password;
    if (password == Acc_password[index]) {
        cout << "Login successful!" << endl;
        cout << "Welcome Back, " << Acc_name[index] << endl;
        cout << "Your account number is: " << Acc_num[index] << endl;
        cout << "Your current balance is: " << Acc_balance[index] << endl;
        return true;
    } else {
        cout << "Incorrect password! Please create an account or re-enter correct credentials." << endl;
        return false;
    }
}

void accountCreation() {
    if (totalAccounts >= 10) {
        cout << "Cannot create more accounts, limit reached!" << endl;
        return;
    }
    cout << "Enter your Name: ";
    cin >> Name;
    cout << "Enter your Surname: ";
    cin >> Surname;
    double cnic, phone_number;
    cout << "Enter your CNIC: ";
    cin >> cnic;
    cout << "Enter your Phone number: ";
    cin >> phone_number;
    int password, confirm_password;

    while (true) {
        cout << "Enter your 4-digit Password: ";
        cin >> password;
        cout << "Confirm Password: ";
        cin >> confirm_password;
        if (password >= 1000 && password <= 9999) {
            if (password == confirm_password) {
                cout << "Password Confirmed!" << endl;
                Acc_num[totalAccounts] = cnic;
                Acc_name[totalAccounts] = Name + " " + Surname;
                Acc_balance[totalAccounts] = 0.0;
                Acc_password[totalAccounts] = password;
                totalAccounts++;
                cout << "Your account is created successfully!" << endl;
                break;
            } else {
                cout << "Passwords do not match!" << endl;
            }
        } else {
            cout << "Invalid password! It must be a 4-digit number." << endl;
        }
    }
}

void performTransaction(int option, int index, float &balance, float &currentBalance) {
    if (option == 1) {
        int amount;
        cout << "Enter amount to deposit: ";
        cin >> amount;
        if (amount > 0) {
            balance += amount;
            Acc_balance[index] = balance;
            currentBalance = balance;
            cout << "Deposit successful!" << endl;
            cout << "Remaining Balance: " << currentBalance << endl;
        } else {
            cout << "Invalid amount!" << endl;
        }
    } else if (option == 2) {
        int amount;
        cout << "Enter amount to withdraw: ";
        cin >> amount;
        if (amount > 0 && amount <= WITHDRAW_LIMIT) {
            if (amount <= balance) {
                balance -= amount;
                Acc_balance[index] = balance;
                currentBalance = balance;
                cout << "Withdrawal successful!" << endl;
                cout << "Remaining Balance: " << currentBalance << endl;
            } else {
                cout << "Not enough balance!" << endl;
            }
        } else {
            cout << "Amount exceeds withdrawal limit of " << WITHDRAW_LIMIT << "!" << endl;
        }
    } else if (option == 3) {
        cout << "Current Balance: " << currentBalance << endl;
    }
}

void showMainMenu() {
    cout << "********************************************************************************" << endl;
    cout << "                  WELCOME TO BANK MANAGEMENT SYSTEM" << endl;
    cout << "********************************************************************************" << endl;
    cout << "1. LOGIN TO YOUR ACCOUNT" << endl;
    cout << "2. CREATE A NEW ACCOUNT" << endl;
    cout << "3. EXIT PROGRAM" << endl;
    cout << "Enter your choice: ";
}

int main() {
    while (true) {
        showMainMenu();
        int choice;
        cin >> choice;

        if (choice == 1) {
            double cnicInput;
            cout << "Enter your CNIC: ";
            cin >> cnicInput;
            if (login(cnicInput)) {
                int index = findAccount(cnicInput);
                float balance = Acc_balance[index];
                float currentBalance = balance;

                while (true) {
                    cout << "\n=== Sub Menu ===" << endl;
                    cout << "1. Deposit Money" << endl;
                    cout << "2. Withdraw Money" << endl;
                    cout << "3. Check Balance" << endl;
                    cout << "4. Exit" << endl;
                    cout << "Enter your option (1-4): ";
                    int option;
                    cin >> option;

                    if (option >= 1 && option <= 3) {
                        performTransaction(option, index, balance, currentBalance);
                    } else if (option == 4) {
                        cout << "Thank you for using the system!" << endl;
                        break;
                    } else {
                        cout << "Invalid choice! Please enter 1-4." << endl;
                    }
                }
            }
        } else if (choice == 2) {
            accountCreation();
        } else if (choice == 3) {
            cout << "Thank you for using Bank Management System!" << endl;
            break;
        } else {
            cout << "Invalid choice! Please enter 1-3." << endl;
        }
    }
    return 0;
}