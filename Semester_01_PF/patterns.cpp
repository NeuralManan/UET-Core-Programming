#include<iostream>
using namespace std;

int main() {
    int n;
    cout<< "enter no. of lines: ";
    cin>> n;
    for(int i=0;i<n;i++){
        for(int j=0;j<i;j++){
            cout<<"*";
        }
        cout<<endl;
    }


    cout<<endl <<endl<<endl;


    for (int i=0; i<n; i++) {
        for (int j=n; j>0; j--) {
            cout << "*";
        }
        cout << endl;
    }

   cout<<endl <<endl<<endl;

    
    for (int i = 0; i < n; i++) {
        // Print leading spaces
        for (int space = 0; space < i; space++) {
            cout << " ";
        }
        // Print stars
        for (int star = 0; star < n - i; star++) {
            cout << "*";
        }
        cout << endl;
    }

    return 0;



       cout<<endl <<endl<<endl;

    
    for (int i = 0; i < n; i++) {
        // Print leading spaces
        for (int space = n; space > 0; space--) {
            cout << " ";
        }
        // Print stars
        for (int star = 1; star <=i; star++) {
            cout << "*";
        }
        cout << endl;
    }

    return 0;
}

