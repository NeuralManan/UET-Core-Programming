#include<iostream>
#include<windows.h>
using namespace std;

void gotoxy(int x, int y);
void printMaze();
void playerMove(int x, int y);

main()
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
       (y = 1);
    }
    if(x == 25)
    {
      (x = 1);
    }
   
   
   
 }
    gotoxy(0, 20);
   
}
void playerMove(int x, int y)
{
     gotoxy(x, y);
     cout<<"P";
     Sleep(200);
     gotoxy(x, y);
     cout<<" ";
     
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