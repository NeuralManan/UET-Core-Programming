#include <iostream>
using namespace std;

int main() {
    int num;
    cout << "Enter the number of elements (n >= 8): ";
    cin >> num;

    int input[100];
    cout << "Enter " << num << " elements:" << endl;
    for (int i = 0; i < num; i++) {
        cin >> input[i];
    }
    
    int reversed[100];
    for (int i = 0; i < num; i++) {
        reversed[i] = input[num - 1 - i];
    }
    
    cout << "Original array: ";
    for (int i = 0; i < num; i++) {
        cout << input[i] << " ";
    }
    cout << endl;
    
    cout << "Reversed array: ";
    for (int i = 0; i < num; i++) {
        cout << reversed[i] << ",";
    }
    cout << endl;
    
    return 0;
}