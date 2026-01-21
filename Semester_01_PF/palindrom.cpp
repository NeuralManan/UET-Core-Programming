#include <iostream>
#include <string>
using namespace std;

bool isPalinDrome(string s) {
    int st = 0, end = s.length() - 1;
    while (st < end) {
        if (s[st++] != s[end--]) {
            return false;
        }
    }
    return true;
}

int main() {
    string input;
    cout << "Enter the string to check whether it is a palindrome or not: \n";
    cin >> input;
    if (isPalinDrome(input)) {
        cout << input << " is a palindrome" << endl;
    } else {
        cout << input << " is not a palindrome" << endl;
    }
    return 0;
}