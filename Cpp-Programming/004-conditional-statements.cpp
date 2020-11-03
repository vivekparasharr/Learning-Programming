//============================================================================
// Name        : 004-conditional-statements.cpp
// Author      : Vivek Parashar
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main() {
	cout << "!!!lets try conditional statements!!!" << endl; // prints !!!Hello World!!!

	/////////// IF STATEMENT ////////////
	string pass="password",pass2;
	cout<<"\n\n--if statement capability--\n";
	cout<<"\nenter password:";
	cin>>pass2;
	if (pass==pass2){
		cout<<"\npassword matches! you can enter!!";
	} else{
		cout<<"\npassword doesnt match! begone!!";
	}

	/////////// IF-ELSE STATEMENT ////////////
	int menuChoice=5;
	cout<<"\n\n--if-else statement capability--\n";
	cout<<"\n1.\tadd record";
	cout<<"\n2.\tdelete record";
	cout<<"\n3.\texit";
	cout<<"\nwhat do you want to do?";
	cin>>menuChoice;
	if (menuChoice==1){
		cout<<"\nlets add some records!!";
	} else if (menuChoice==2){
		cout<<"\nlets delete some records!!";
	} else{
		cout<<"\nexiting! good-bye!!";
	}

	/////////// SWITCH STATEMENT ////////////
	int menuChoice2=5;
	cout<<"\n\n--switch statement capability--\n";
	cout<<"\n1.\tadd record";
	cout<<"\n2.\tdelete record";
	cout<<"\n3.\texit";
	cout<<"\nwhat do you want to do?";
	cin>>menuChoice2;
	switch(menuChoice2){
	case 1:
		cout<<"\nlets add some records!!";
		break;
	case 2:
		cout<<"\nlets delete some records!!";
		break;
	case 3:
		cout<<"\nexiting! good-bye!!";
		break;
	default:
		cout<<"\n!!!!error!!!!";
	}

	/////////// COMPARING FLOAT TYPES - this works ////////////
	cout<<"\n\n--comparing float variables - when it works--\n";
	float height=6.2, height2;
	cout<<"\nenter height:";
	cin>>height2;
	cout<<"height 1:"<<fixed<<height<<" compared with height 2:"<<fixed<<height2<<endl;
	if (height==height2){
		cout<<"height matches!!";
	} else{
		cout<<"height doesnt match!!";
	}

	/////////// COMPARING FLOAT TYPES - this doesnt work because of precision problem ////////////
	// you can cout height3 and see that its value is not actually 6.2, but 6.2000004 or something
	// so when we compare it to 6.2 exact, it doesnt match
	// however in the previous example when we ask the user to enter it and the user enters 6.2, the computer saves it as 6.2000004 or something and that matches exactly. so in that case it works
	cout<<"\n\n--comparing float variables issue - when it doesnt--\n";
	float height3=6.2;
	cout<<"height 3:"<<fixed<<height3<<" compared with value 6.2"<<endl;
	if (height3==6.2){
		cout<<"height matches!!";
	} else{
		cout<<"height doesnt match!!";
	}

	// not equal operator !=
	//we can combine multiple conditions using && or ||. example, condition 1 && condition 2
	// we can use bool like following to check the result of multiple conditions
	// bool conditionOutput = ( ( condition1 && condition2 ) || condition3 )

	return 0;
}
