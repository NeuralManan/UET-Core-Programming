#include <iostream>
using namespace std;
float price;
main(){
string movies[5] =  {"Gladiator", "StarWars", "Terminator", "TakingLives", "TombRider"}, choice;
cout<<" Enter the movie name (Gladiator, StarWars, Terminator, TakingLives, TombRider): "<<endl;
cin>>choice;
if(choice == movies[1]){
cout<<" Total ticket price is: 500 PKR"<<endl;
price = 500 - 25;
cout<< "The discounted price after 5% discount is: "<<price;
}
else if(choice == movies[3]){
cout<<" Total ticket price is: 500 PKR"<<endl;
price = 500 - 25;
cout<< "The discounted price after 5% discount is: "<<price;
}
else{
cout<<"Total ticket price is: 500 PKR" <<endl;
int price;
price = 500 - 50;
cout<< "The discounted price after 10% discount is: "<<price;
}
}

