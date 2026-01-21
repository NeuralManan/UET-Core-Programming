#include <iostream> 
#include <cstdlib>  // for rand() 
using namespace std;
int gnumber; 

int main() { 
// Generate a random number between 1 and 100 
int randomNumber = rand() % 100 + 1; 
cout << "Random Number: " << randomNumber << endl; 

cout<<"Guess the random number: ";
cin>>gnumber;

while(gnumber != randomNumber){

if(randomNumber-gnumber > 10){cout<<" you are too away from the number."<<endl;}
else if(randomNumber-gnumber < 10){cout<<" you are very close to the number."<<endl;}      
else if(randomNumber-gnumber == 0){
cout<<" yes you are right."<<endl;

}
cin>>gnumber;
}
}