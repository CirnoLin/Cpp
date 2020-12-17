#include <iostream>
#include <string>
using namespace std;

int main(){
	string binary;
	int len,temp;
	cin>>binary;
	len=binary.length();
	int bin[len-1];
	temp=len;
	for (;temp>0;temp--){
		bin[temp-1]=binary[temp-1];
	}
	cout<<bin[len-1]<<endl;
	return 0;
}
