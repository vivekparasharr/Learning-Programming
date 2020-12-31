
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

# The Repeat loop executes the same code again and again until a stop condition is met.
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

Live Demo

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
# Extracting parts of a string - substring() function
# Syntax
substring(x,first,last)
# Example - Extract characters from 5th to 7th position.
result <- substring("Extract", 5, 7)
print(result)


# R - Vectors
