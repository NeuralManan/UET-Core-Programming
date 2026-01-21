#include <iostream>
using namespace std;

void printUpperPart(int rows) {
    for (int i = 1; i <= rows; i++) {
        for (int j = 1; j <= i; j++) {
            cout << "* ";
        }
        cout << endl;
    }
}

void printLowerPartReverse(int rows) {
    for (int i = rows; i >= 1; i--) {
        for (int j = 1; j <= i; j++) {
            cout << "* ";
        }
        cout << endl;
    }
}

int main() {
    int numRows;
    cout << "Enter desired number of rows: ";
    cin >> numRows;
    printUpperPart(numRows);
    printLowerPartReverse(numRows);
    return 0;
}