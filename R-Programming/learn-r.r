
myString <- "Hello, World!"
print (myString)

# The variables can be assigned values using leftward (<-), rightward (->) and equal (=) to operator. 
# Assignment using equal operator.
var.1 = c(0,1,2,3)           
# Assignment using leftward operator ( <- , <<- )
var.2 <- c("learn","R")   
# Assignment using rightward operator ( -> , ->> )
c(TRUE,1) -> var.3           

# The values of the variables can be printed using print() or cat() function. The cat() function combines multiple items into a continuous print output.
print(var.1)
cat ("var.1 is ", var.1 ,"\n")

# Finding Variables - To know all the variables currently available in the workspace we use the ls() function. Also the ls() function can use patterns to match the variable names.
print(ls())
# List the variables starting with the pattern "var".
print(ls(pattern = "var"))   
# The variables starting with dot(.) are hidden, they can be listed using "all.names = TRUE" argument to ls() function.

# Delete variables - Variables can be deleted by using the rm() function
rm(var.3)
print(var.3)
# All the variables can be deleted by using the rm() and ls() function together.
rm(list = ls())
print(ls())


# There are many types of R-objects. The frequently used ones are −
# Logical
v <- TRUE 
print(class(v))
# Numeric
v <- 23.5
print(class(v))
# Integer
v <- 2L
print(class(v))
# Complex
v <- 2+5i
print(class(v))
# Character
v <- "TRUE"
print(class(v))
# Raw
v <- charToRaw("Hello")
print(class(v))

# Vectors - When you want to create vector with more than one element, you should use c() function which means to combine the elements into a vector.
# Create a vector.
apple <- c('red','green',"yellow")
print(apple)
# Get the class of the vector.
print(class(apple))

# Lists - A list is an R-object which can contain many different types of elements inside it like vectors, functions and even another list inside it.
# Create a list.
list1 <- list(c(2,5,3),21.3,sin)
# Print the list.
print(list1)

# Matrices - A matrix is a two-dimensional rectangular data set. It can be created using a vector input to the matrix function.
# Create a matrix.
M = matrix( c('a','a','b','c','b','a'), nrow = 2, ncol = 3, byrow = TRUE)
print(M)

# Arrays - While matrices are confined to two dimensions, arrays can be of any number of dimensions. The array function takes a dim attribute which creates the required number of dimension. In the below example we create an array with two elements which are 3x3 matrices each.
# Create an array.
a <- array(c('green','yellow'),dim = c(3,3,2))
print(a)

# Factors - Factors are the r-objects which are created using a vector. It stores the vector along with the distinct values of the elements in the vector as labels. The labels are always character irrespective of whether it is numeric or character or Boolean etc. in the input vector. They are useful in statistical modeling. Factors are created using the factor() function. The nlevels functions gives the count of levels.
# Create a vector.
apple_colors <- c('green','green','yellow','red','red','red','green')
# Create a factor object.
factor_apple <- factor(apple_colors)
# Print the factor.
print(factor_apple)
print(nlevels(factor_apple))

# Data frames are tabular data objects. Unlike a matrix in data frame each column can contain different modes of data. The first column can be numeric while the second column can be character and third column can be logical. It is a list of vectors of equal length. Data Frames are created using the data.frame() function.
# Create the data frame.
BMI <- 	data.frame(
   gender = c("Male", "Male","Female"), 
   height = c(152, 171.5, 165), 
   weight = c(81,93, 78),
   Age = c(42,38,26)
)
print(BMI)


# Types of Operators - We have the following types of operators in R programming −
# Arithmetic Operators
v <- c( 2,5.5,6)
t <- c(8, 3, 4)
print(v+t) # Adds two vectors
print(v-t) # Subtracts second vector from the first
print(v*t) # Multiplies both vectors
print(v/t) # Divide the first vector with the second
print(v%%t) # Give the remainder of the first vector with the second
print(v%/%t) # The result of division of first vector with second (quotient)
print(v^t) # The first vector raised to the exponent of second vector
# Relational Operators ( > , < , == , <= , >= , != )
# Logical Operators
# & , | , ! - element of the first vector is compared with the corresponding element of the second vector. The result of comparison is a Boolean value.
# && , || - considers only the first element of the vectors and give a vector of single element as output.
# Assignment Operators ( <- , <<- , = , -> , ->> )
# Miscellaneous Operators
# : (Colon operator). It creates the series of numbers in sequence for a vector.
v <- 2:8
print(v)  # [1] 2 3 4 5 6 7 8
# %in% - This operator is used to identify if an element belongs to a vector.
v1 <- 12
t <- 1:10
print(v1 %in% t) 


# Conditional - R provides the following types of decision making statements. 
# The basic syntax for creating an if statement in R is −
if (test_expression) {
statement
}
# Example
x <- 5
if(x > 0){
print("Positive number")
}

# The basic syntax for creating an if...else statement in R is −
if (test_expression) {
statement1
} else {
statement2
}
# Example
x <- -5
if(x > 0){
print("Non-negative number")
} else {
print("Negative number")
}

# The basic syntax for creating an if...else if...else statement in R is −
if (test_expression1) {
statement1
} else if (test_expression2) {
statement2
} else if (test_expression3) {
statement3
} else {
statement4
}
# Example
x <- 0
if (x < 0) {
print("Negative number")
} else if (x > 0) {
print("Positive number")
} else
print("Zero")

# A switch statement allows a variable to be tested for equality against a list of values. Each value is called a case, and the variable being switched on is checked for each case.
x <- switch(
   2,
   "first",
   "second",
   "third",
   "fourth"
)
print(x)


# R - Loops
# A loop statement allows us to execute a statement or group of statements multiple times

# The Repeat loop executes the same code again and again until a stop condition is met.
# Syntax
repeat { 
   commands 
   if(condition) {
      break
   }
}
# Example
v <- c("Hello","loop")
cnt <- 2
repeat {
   print(v)
   cnt <- cnt+1   
   if(cnt > 5) {
      break
   }
}

# The While loop executes the same code again and again until a stop condition is met.
# Syntax
while (test_expression) {
   statement
}
# Example
v <- c("Hello","while loop")
cnt <- 2
while (cnt < 7) {
   print(v)
   cnt = cnt + 1
}

# The for loop
# Syntax
for (value in vector) {
   statements
}
# Example
v <- LETTERS[1:4]
for ( i in v) {
   print(i)
}

# When the break statement is encountered inside a loop, the loop is immediately terminated and program control resumes at the next statement following the loop.
# On encountering next, the R parser skips further evaluation and starts next iteration of the loop.


# An R function is created by using the keyword function. 
# Syntax
function_name <- function(arg_1, arg_2, ...) {
   Function body 
}
# Example
# Create a function to print squares of numbers in sequence.
new.function <- function(a) {
   for(i in 1:a) {
      b <- i^2
      print(b)
   }
}
# Call the function new.function supplying 6 as an argument.
new.function(6)


# Create a function with arguments.
new.function <- function(a = 3, b = 6) {
   result <- a * b
   print(result)
}
# Call the function without giving any argument.
new.function()
# Call the function with giving new values of the argument.
new.function(9,5)


# Strings
# Any value written within a pair of single quote or double quotes in R is treated as a string. 
# Concatenate strings
pastestr1, str2, str3, ... , sep = " ", collapse = NULL)

# Formatting - Numbers and strings can be formatted to a specific style using format() function.
# Syntax
format(x, digits, nsmall, scientific, width, justify = c("left", "right", "centre", "none")) 
# Example
# Total number of digits displayed. Last digit rounded off.
result <- format(23.123456789, digits = 9)
print(result)
# Display numbers in scientific notation.
result <- format(c(6, 13.14521), scientific = TRUE)
print(result)
# The minimum number of digits to the right of the decimal point.
result <- format(23.47, nsmall = 5)
print(result)
# Format treats everything as a string.
result <- format(6)
print(result)
# Numbers are padded with blank in the beginning for width.
result <- format(13.7, width = 6)
print(result)
# Left justify strings.
result <- format("Hello", width = 8, justify = "l")
print(result)
# Justfy string with center.
result <- format("Hello", width = 8, justify = "c")
print(result)


# Counting number of characters in a string - nchar() function
nchar(test_str)

# Changing the case - toupper() & tolower() functions
str = 'apPlE'
toupper(str) # APPLE
tolower(str) # apple
# Extracting parts of a string - substring() function
# Syntax
substring(x,first,last)
# Example - Extract characters from 5th to 7th position.
result <- substring("Extract", 5, 7)
print(result)


# R - Vectors
# Single Element Vector
v <- "abc"

# Multiple Elements Vector
v <- 5:13
v <- seq(5, 13, by = 1)

# Using the c() function
Live Demo

# The logical and numeric values are converted to characters.
v <- c('apple','red',5,TRUE)

v <- c("Sun","Mon","Tue","Wed","Thu","Fri","Sat")
print(v[c(2,3,6)])
print(v[c(FALSE,TRUE,TRUE,FALSE,FALSE,TRUE,FALSE)])
print(v[c(-1,-4,-5,-7)])

# Vector Manipulation
# Vector arithmetic - Two vectors of same length can be added, subtracted, multiplied or divided giving the result as a vector output.
# If we apply arithmetic operations to two vectors of unequal length, then the elements of the shorter vector are recycled to complete the operations.
v1 <- c(2,3,4,5,6,7)
v2 <- c(1,2)
# V2 becomes c(1,2,1,2,1,2)
result = v1 + v2

# Vector Element Sorting
sort(v, decreasing = TRUE)


# R - Lists
# Lists are the R objects which contain elements of different types like − numbers, strings, vectors and another list inside it. A list can also contain a matrix or a function as its elements. List is created using list() function.
# Creating a List
list_data <- list("Red", c(21,32,11), TRUE, 51.23)
# Give names to the elements in the list.
names(list_data) <- c("color", "nested_list", "boolean_value", "decimal_number")
# Accessing List Elements
list_data[1] # "Red"
list_data["color"] # Red
list_data$color # Red
# Access elements of a nested list
l2 = list(c(1,2,3), c(4,5,6), nrows=2
l2[[1]] # To access a nested list we use double square brackets to provide position of element: [[position]]
l2[[2]][1] # 4

# Manipulating List Elements
# Add element at the end of the list.
list_data[4] <- "New element"
# Remove the last element.
list_data[4] <- NULL
# Update the 3rd Element.
list_data[3] <- "updated element"

# Merging Lists
l1 = list(1,2,3)
l2 = list(4,5,6)
merged_list = c(l1, l2) 
# print(merged_list[1]) # returns element 1
merged_list_of_list = list(l1, l2) 
# print(merged_list_of_list[1]) # returns l1
# print(merged_list_of_list[[1]][1]) # returns element 1

# Converting List to Vector using unlist() function.
l1 <- list(1:3)
l2 <-list(4:6)
# l1 + l2 # shows an error because this is not  vector so arithmetic operations are not possible
unlist(l1) + unlist(l2) # 5 7 9 


#  R - Matrices
# matrix(data, nrow, ncol, byrow, dimnames)
M <- matrix(c(3:14), nrow = 4, byrow = TRUE)
# Define the column and row names.
rownames = c("row1", "row2", "row3", "row4")
colnames = c("col1", "col2", "col3")
P <- matrix(c(3:14), nrow = 4, byrow = TRUE, dimnames = list(rownames, colnames))

# Accessing Elements of a Matrix
print(P[4,2]) # Access the element at 2nd column and 4th row.
print(P[2,]) # Access only the  2nd row.
print(P[,3]) # Access only the 3rd column.

# Matrix Computations
# Create two 2x3 matrices.
m1 <- matrix(c(3, 9, -1, 4, 2, 6), nrow = 2)
m2 <- matrix(c(5, 2, 0, 9, 3, 4), nrow = 2)
m1 + m2 # Add the matrices.
m1 - m2 # Subtract the matrices
m1 * m2 # Multiply the matrices.
m1 / m2 # Divide the matrices


# R - Arrays
# An array is created using the array() function. It takes vectors as input and uses the values in the dim parameter to create an array.
# For example − If we create an array of dimension (2, 3, 4) then it creates 4 rectangular matrices each with 2 rows and 3 columns.
# dim=c(rows, columns, matrices)
array2 = array(1:12, dim=c(2, 3, 2))
# Naming Columns and Rows
column.names <- c("COL1","COL2","COL3")
row.names <- c("ROW1","ROW2")
matrix.names <- c("Matrix1","Matrix2")
array2 = array(1:12, dim=c(2, 3, 2), dimnames = list(row.names, column.names, matrix.names))

# Accessing Array Elements
# dim=c(rows, columns, matrices)
print(array2[2,,2]) # Print the second row of the second matrix of the array.
print(array2[1,3,1]) # Print the element in the 1st row and 3rd column of the 1st matrix.
print(array2[,,2]) # Print the 2nd Matrix.
# Since the returned values here are matrices, we can perform matrix operations on them
# As array is made up matrices in multiple dimensions, the operations on elements of array are carried out by accessing elements of the matrices.

# Calculations Across Array Elements
# we can use user defined functions as well
# summary
# apply(X, MARGIN, FUN) - apply to r or c or both - input to this funciton is a df - output is a vector, list or array
m1 <- matrix(C<-(1:10),nrow=5, ncol=2)
apply(m1, 2, sum)
# lapply(X, FUN) - apply to all elements - input to this function is list, vector or df - output is a list
# sapply(X, FUN) - apply to all elements - input to this function is list, vector or df - output is a vector or a matrix
movies <- c("BRAVEHEART","BATMAN","VERTIGO","GANDHI")
lapply(movies, tolower)
sapply(movies, tolower)
# tapply(X, INDEX, FUN = NULL) - apply to each factor variable in a vector - input to this function is a vector - output it an array
data(iris)
tapply(iris$Sepal.Width, iris$Species, median)


# R - Factors
# Factors are the data objects which are used to categorize the data and store it as levels. They can store both strings and integers. They are useful in the columns which have a limited number of unique values. Like "Male, "Female" and True, False etc. They are useful in data analysis for statistical modeling. Factors are created using the factor () function by taking a vector as input.
data <- c("East","West","East","North","North","East","West","West","West","East","North")
print(data) # shows the vector
factor_data <- factor(data, levels = c("East","West","North")) # Optional to specify a custom order for factor levels
is.factor(factor_data)
print(factor_data) # shows that there are three levels: East North West

# Generating Factor Levels
# gl(number_of_levels, number_of_replications, labels)
# Example
gl(3, 4, labels = c("India", "Chile","Canada"))

# R - Data Frames
# A data frame is a table or a two-dimensional array-like structure in which each column contains values of one variable and each row contains one set of values from each column.
df <- data.frame(
   emp_id = c (1:5), 
   emp_name = c("Vivek","Harry","Tony","Bruce","Clark"),
   salary = c(9500.0,6200.5,7400.5,8800.0,12000.25), 
   start_date = as.Date(c("2011-02-01", "2012-10-15", "2013-08-25", "2016-06-21", "2018-02-28")),
   stringsAsFactors = FALSE
)
print(df)

str(df) # see structure of the data frame
summary(df) # see statistical summary and nature of the data 

# Extract Specific columns.
result <- data.frame(df$emp_name,df$salary)
# Extract first two rows.
result <- df[1:2,]
# Extract 3rd and 5th row with 2nd and 4th column.
result <- df[c(3,5),c(2,4)]

# Expand Data Frame
# Add Column
df$age <- c(30, 40, 50, 35, 45)
# Add Row using rbind
df3 <- rbind(df1,df2)


# R - Packages
install.packages("Package Name") # Install a New Package
install.packages(file_name_with_path, repos = NULL, type = "source") # Install package manually
library("package Name") # Load Package 
library() # Get the list of all the packages installed
search() # Get all packages currently loaded in the R environment


# R - Data Reshaping
# Joining Columns and Rows in a Data Frame
# cbind() - join multiple vectors to create a data frame
name = c('clark', 'harry', 'tony', 'bruce')
age = c(10,20,30,40)
height = c( 185, 170, 175, 180)
students = data.frame(cbind(name, age, height))
print(students)
# rbind() - merge two data frames
students_new = c('vivek', 30, 185)
students = rbind(students, students_new)
print(students)
# Merging Data Frames - column names on which the merging happens should be the same
df1 = data.frame(name=c('apple', 'orange', 'banana'), color=c('red', 'orange', 'yellow'), stringsAsFactors = FALSE)
df2 = data.frame(name=c('apple', 'orange', 'banana'), weight=c(250, 230, 210), stringsAsFactors = FALSE)
print(df1)
print(df2)
print(merge(x=df1, y=df2, by.x=c('name','name'), by.y=c('name','name')))
# by default merge i ssame as inner join

# Melting and Casting
library(reshape2)
df = data.frame(name=c('apple','orange','banana'), color=c('red','orange','yellow'), count=c(50,60,70), weight=c(250, 230, 210), stringsAsFactors = FALSE)
# melt - converting columns into multiple  rows; basically wide to long format
molten_df = melt(df, id=c('name','color')) # Any variables not specified will be melted
# cast - converting multiple rows into columns; basically long to wide format
dcast(molten_df, name+color~variable,sum) # dcast returns a dataframe, acast returns array or matrix



# Reading a CSV File
data <- read.csv("input.csv")
# Writing into a CSV File
write.csv(data,"output.csv") # optional - , row.names = FALSE
# Reading the Excel File
install.packages("xlsx")
data <- read.xlsx("input.xlsx", sheetIndex = 1)
# Reading the JSON File
install.packages("rjson")
result <- fromJSON(file = "input.json")
json_data_frame <- as.data.frame(result)


# classes
# We will cover s4 classes here. S4 class is defined by the setClass() method. 
setClass("emp_info", slots=list(name="character", age="numeric", contact="character"))
emp1 <- new("emp_info",name="vivek", age=30, contact="somehwere on the internet")

# Access elements of a class
emp1@name

