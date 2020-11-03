//============================================================================
// Name        : 003-strings.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
//#include <string>
using namespace std;

int main() {
	string myname="vivek parashar";
	string fname="viv", lname="par", flname;
	flname=fname + " " + lname; //concatenate
	cout << "my name is " << myname;
	cout << "\nshort name " << flname;

	string yourName;
	cout << "\n\nwhat is your name? ";
	cin >> yourName;
	cout <<"\nnice to meet you "<<yourName;
	return 0;
}
