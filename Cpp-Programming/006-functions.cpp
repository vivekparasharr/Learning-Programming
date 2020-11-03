//============================================================================
// Name        : 006-functions.cpp
// Author      : Vivek Parashar
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>

#include "006-utils.h"

using namespace std;

int hello_world() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	return 0;
}

int start_journey() {
	cout << "!!!Lets start with your C++ journey!!!" << endl;
	return 0;
}

int main_menu() {
	int choice=4;
	cout << "\n1. Add";
	cout << "\n2. View";
	cout << "\n3. Delete";
	cout << "\n4. Exit";
	cout << "\nEnter your choice:";
	cin>>choice;
	return choice;
}

int sub_menu(int choice); // this is a function prototype and the actual function will be defined later
//this allows the compiler to execute the code even though the actual function is defined after the main()

int main() {
	hello_world();
	start_journey();
	int choice1=4, junk;
	choice1=main_menu();
	cout<<"\nYou chose:"<<choice1;
	junk = sub_menu(choice1);
	cout<<"\nExiting! Goodbye from main!!  "<<junk;
	doSomething();
	return 0;
}

int sub_menu(int choice) {
	switch(choice){
		case 1:
			cout<<"\nLets add a new record";
			break;
		case 2:
			cout<<"\nLets view an existing record";
			break;
		case 3:
			cout<<"\nLets delete an existing record";
			break;
		default:
			cout<<"\nExiting! Goodbye!!";
	}
	return 0;
}

