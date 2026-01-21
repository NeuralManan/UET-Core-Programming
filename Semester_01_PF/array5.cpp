#include <iostream>
using namespace std;
int main(){
string sentence;
cout<<"enter sentence: ";
cin>>sentence;
string sentence2;
int count = 0;
for(int i=0; i<16; i++){
if(sentence[i] !='a' && sentence[i] !='e' && sentence[i] !='i' && sentence[i] !='o' && sentence[i] !='u')
{
sentence2[count]=sentence[i];
count++;
cout<<sentence[i];
}
}
}