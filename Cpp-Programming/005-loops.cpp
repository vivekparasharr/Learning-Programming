//============================================================================
// Name        : 005-loops.cpp
// Author      : Vivek Parashar
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main() {
	cout << "!!!loops!!!" << endl; // prints !!!Hello World!!!

	int i=1;
	//////////// while loop /////////////
	cout<<"\n\nwhile loop - first 10 natural numbers"<<endl;
	while (i<=10){
		cout<<i<<", ";
		i+=1; //same as i=i+1 or i+=1
	}

	//first 10 fibonacci numbers
	i=1;
	int j=1,k=1,l=1;
	cout<<"\n\nwhile loop - first 10 natural numbers"<<endl;
	while (i<=10){
		cout<<j<<", ";
		i++;
		l=j;
		j=k;
		k=k+l;
	}

	//////////// do-while loop /////////////
	//atleast the content of the loop is executed once before checking the condition
	//for example if you want the user to enter the password again and again until they enter the correct password
	//but no matter what, you atleast want the use to enter the password once
	cout<<"\n\ndo-while loop\n";
	i=1;
	string pass="pass", pass2;
	do{
		if(i!=1){
			cout<<"\naccess denied, try again";
		}
		cout<<"\nenter your password?";
		cin>>pass2;
		i=0;
	}while(pass2 != pass);
	cout<<"\npassword accepted\n\n";

	//////////// for loop /////////////
	cout<<"\nfor loop\n";
	for(int f=1;f<11;f++){
		cout<<f<<", ";
	}

	//break jumps immidiately out of the loop. mostly used in while loops but can also be used in for loops
	cout<<"\nbreak statement\n";
	for(int f=1;f<11;f++){
		if(f==5){
			break; //we break out of the loop when f==5, and dont execute the loop for f>=5
		}
		cout<<f<<", ";
	}

	//continue is similar to break, but just breaks out of the current iteration, but still continues running the next iterations
	cout<<"\nbreak statement\n";
	for(int f=1;f<11;f++){
		if(f==5){
			continue;
		}
		cout<<f<<", "; //this statement not executed for f==5
	}

	return 0;
}
