#include <iostream>
using namespace std;
bool check =true;
int main() {
char num[4];

for(int i=0; i<4; i++){
cout<<" enter the character: ";
cin>>num[i];


if(num[0] != num[i]){
check = false;
}
}

if(check == true){
cout<<" true";
}

else{
cout<<" false ";

}
}