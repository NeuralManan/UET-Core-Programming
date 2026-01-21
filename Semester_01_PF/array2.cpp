#include <iostream>
using namespace std;
int main(){
string word;
cout<<" enter a word: ";
cin>>word;
char dig;
cout<<" enter the letter: ";
cin>>dig;
for(int i=0; word[i] != '\0'; i++){
if(word[i] == dig){
cout<<dig<<" is found at position "<<i<<endl;

}
}
}