
/* import csv */
/* GETNAME= is set to 'no', so the variable names in record 1 are not used */
proc import datafile='/folders/myfolders/predict_churning_customers/BankChurners.csv'
     out=bankchurners
     dbms=csv
     replace;
     getnames=yes;
run;

/* show imported data */
proc print data=bankchurners;
run;

* create a copy of a table ;
data bankchurners_copy;
	set bankchurners;
run;
