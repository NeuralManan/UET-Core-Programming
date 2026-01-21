#include<iostream>
#include<windows.h>
using namespace std;

void gotoxy(int x, int y);
void printMaze();
void playerMove(int x, int y);

int main()  // 'main' should return int, not be void
{
    int x = 1, y = 1;
    system("cls");
    printMaze();
    while (true)
    {
        playerMove(x, y);
        x = x + 3;
        y = y + 1;
        if(y == 9)
        {
            y = 1;  // Remove parentheses, just use assignment
        }
        Sleep(200);  // Capital 'S' for Windows Sleep function
        playerMove(x, y);
        x = x - 3;
        y = y - 1;
        if(x == 25)
        {
            x = 9;  // Remove parentheses, just use assignment
        }
    }
    gotoxy(0, 20);
    return 0;  // Add return statement for main
}

void playerMove(int x, int y)
{
    gotoxy(x, y);
    cout << "P";
    Sleep(200);
    gotoxy(x, y);
    cout << " ";
}

void gotoxy(int x, int y)
{
    COORD coordinates;
    coordinates.X = x;
    coordinates.Y = y;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coordinates);
}

void printMaze()
{
    cout << "###########################" << endl;
    cout << "#                         #" << endl;
    cout << "#                         #" << endl;
    cout << "#                         #" << endl;
    cout << "#                         #" << endl;
    cout << "#                         #" << endl;
    cout << "#                         #" << endl;
    cout << "#                         #" << endl;
    cout << "#                         #" << endl;
    cout << "#                         #" << endl;
    cout << "###########################" << endl;
}