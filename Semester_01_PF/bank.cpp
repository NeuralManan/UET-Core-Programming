#include <iostream>
#include <string>
using namespace std;

const int WITHDRAW_LIMIT = 300000;

int Acc_num[10] = {12345678, 98765432}; // Increased array size for new accounts

string Acc_name[10] = {"ali", "Wahab"};

float Acc_balance[10] = {100000, 200000};

int Acc_password[10] = {1234, 5678}; // Store passwords

int totalAccounts = 2; // Track number of accounts

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
        cout << "Account not found!" << endl;
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
        cout << "Incorrect password!" << endl;
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













int main() {
    cout << "*" << endl;
    cout << "           Welcome to the Bank of UET                    " << endl;
    cout << "*" << endl;

    while (true) {
        cout << "\n=== Login Menu ===" << endl;
        cout << "1. Deposit Money" << endl;
        cout << "2. Withdraw Money" << endl;
        cout << "3. Check Balance" << endl;
        cout << "4. Login to Account" << endl;
        cout << "5. Create New Account" << endl;
        cout << "6. Exit" << endl;
        cout << "Enter your option (1-6): ";
        int choice;
        cin >> choice;

        double cnicInput;
        int index;
        float balance = 0.0;
        float currentBalance = 0.0;

        if (choice >= 1 && choice <= 3) {
            cout << "Enter your CNIC: ";
            cin >> cnicInput;
            if (login(cnicInput)) {
                index = findAccount(cnicInput);
                balance = Acc_balance[index];
                currentBalance = balance;
                performTransaction(choice, index, balance, currentBalance);
            }
        } else if (choice == 4) {
            cout << "Enter your CNIC: ";
            cin >> cnicInput;
            if (login(cnicInput)) {
                index = findAccount(cnicInput);
                balance = Acc_balance[index];
                currentBalance = balance;

                while (true) {
                    int option;
                    cout << "=== Main Menu ===" << endl;
                    cout << "1. Deposit Money" << endl;
                    cout << "2. Withdraw Money" << endl;
                    cout << "3. Check Balance" << endl;
                    cout << "4. Logout" << endl;
                    cout << "Enter your option (1-4): ";
                    cin >> option;

                    if (option >= 1 && option <= 3) {
                        performTransaction(option, index, balance, currentBalance);
                    } else if (option == 4) {
                        cout << "Logged out successfully!" << endl;
                        break;
                    } else {
                        cout << "Invalid choice! Please enter 1-4." << endl;
                    }
                }
            }
        } else if (choice == 5) {
            accountCreation();
        } else if (choice == 6) {
            cout << "Thank you for using Bank of UET!" << endl;
            break;
        } else {
            cout << "Invalid choice! Please enter 1-6." << endl;
        }
    }
    return 0;
}