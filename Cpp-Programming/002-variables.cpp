/*
 * 002-variables.cpp
 *
 *  Created on: Jul 18, 2020
 *      Author: vivek
 */

#include<iostream>
#include<climits> //maximum values of variable types can  be found in this
#include<iomanip> //input output manipulation
using namespace std;
int main(){

	int numberCats=5,numberCats2=0,totalCats=0; //long int can be used for storing large values
	//unsigned int can be used to store positive or negative values
	//short int can be used to store smaller values
	//float variables can be used to store numbers with a decimal point
	cout<<"i have "<<numberCats<<" cats";
	cout<<"\nhow many cats do you have?";
	cin>>numberCats2;
	totalCats=numberCats+numberCats2;
	cout<<"nice!"<<"\nin total we have "<<totalCats<<" cats!";
	cout<<"\nthe size of variable totalCats is: "<<sizeof(totalCats);
	cout<<"\nthe size of float variables is: "<<sizeof(float);

	cout<<"\nmax value of interger type is: "<< INT_MAX ;

	float pi=3.1415926535; //pi=22/7
	cout<<"\n\nvalue of pi: "<<pi;
	cout<<"\n\nvalue of pi: "<<fixed<<pi;
	cout<<"\n\nvalue of pi: "<<scientific<<pi; //google iomanip to see other types

	//we can also alternate the number of significant digits using setprecision
	cout<<"\n\nvalue of pi: "<<setprecision(3)<<pi; //only the value we provided is correct, rest of the digits are just junk values to take the output to 20 significant digits

	//for more significant digits we need to use other variable type than float
	double dValue=3.1415926535;
	cout<<"\nmore precision: "<<dValue<<" , stored using "<<sizeof(double)<<" bytes!";

	long double ldValue=3.1415926535;
	cout<<"\neven more precision: "<<ldValue<<" , stored using "<<sizeof(long double)<<" bytes!";

	bool bval=true; //boolean type is true or false; c++ uses 1 for true and 0 for false when outputting
	cout<<"\n\nboolean value is: "<<bval<<" , stored using "<<sizeof(bool)<<" bytes!";

	char cval=55, cval2='7'; //takes exactly 1 byte of computer memory, char represents single characters from the ascii character set, 55 is the ascii code for 7, this is not the number 7 but the character 7
	cout<<"\n\ncharacter value is: "<<cval<<" , stored using "<<sizeof(char)<<" bytes!";
	cout<<"\n\ncharacter value is: "<<cval2<<" , stored using "<<sizeof(char)<<" bytes!";

	wchar_t wval='7'; //takes exactly 1 byte of computer memory, does the opposite of char in the way that it stores the actual ascii value of the character
	cout<<"\n\nw-character value is: "<<wval<<" , stored using "<<sizeof(char)<<" bytes!";
	cout<<"\n\nw-character value is: "<<(char)wval<<" , stored using "<<sizeof(char)<<" bytes!";

	string myname="vivek parashar";
	string fname="viv", lname="par", flname;
	flname=fname + " " + lname; //concatenate
	cout << "\n\nmy name is " << myname;
	cout << "\nshort name " << flname;

	string yourName;
	cout << "\n\nwhat is your name? ";
	cin >> yourName;
	cout <<"\nnice to meet you "<<yourName<<endl<<endl;

	/////////////////////// ARRAYS //////////////////////
	int ar[3];
	ar[0]=10;
	ar[1]=20;
	ar[2]=30;
	cout<<"\nthis is an array: ";
	for (int i=0;i<3;i++){
		cout<<ar[i]<<", ";
	}

	int ar2[4]={15,25,35,45};
	cout<<"\nthis is an array too: ";
	for (int i=0;i<4;i++){
		cout<<ar2[i]<<", ";
	}

	int ar2Sum=0;
	for (int i=0;i<4;i++){
		ar2Sum+=ar2[i];
	}
	cout<<"\nsum of elements of array ar2: "<<ar2Sum;

	//practice - create an array with a table of 12
	int t12[10];
	for (int i=0;i<10;i++){
		t12[i]=12*(i+1);
	}
	cout<<"\n\ntable of 12, stored in an array\n";
	for (int i=0;i<10;i++){
		cout<<t12[i]<<", ";
	}

	/////////////////////// multidimentional ARRAYS //////////////////////
	int mar[3][2]={
			{34,188},
			{29,165},
			{29,160}
	}; //multi-dim array
	cout<<"\nthis is a multi dimentional array: ";
	for (int i=0;i<3;i++){ //3 rows in the array
		cout<<"\nrow "<<i+1<<":  ";
		for (int j=0;j<2;j++){ //2 columns in the array
			cout<<"col "<<j+1<<": "<<mar[i][j]<<", ";
		}
	}
	cout<<"\n\nthe multi-dimentional array uses "<<sizeof(mar)<<" bytes of storage!";
	//the multi dim array has 3x2=6 integers and each integer requires 4 bytes, so 6x4=24 bytes required in total

	return 0;
}
