
# What is REPL - Read/Evaluate/Print/Loop
# Reads what you type;
# Evaluates it;
# Prints out the return value; then
# Loops back and does it all over again.

# Julia: Start REPL 
# The Julia extension provides a Julia REPL inside VS Code. You can start this REPL with the Julia: Start REPL command.
# There are four commands that you can use to run code from your editor in the Julia REPL:
# Julia: Execute Code (Ctrl+Enter)
# Julia: Execute Code Block (Alt+Enter)
# Julia: Execute Code Cell (Shift+Enter)
# Julia: Execute File


##############################################################################
################################  basics  ####################################
##############################################################################

4+2
4+2; # If you don't want to see the result of the expression printed, use a semicolon at the end of the expression

ans # the value of the last expression you typed on the REPL, it's stored within the variable ans

name = readline(stdin) # receiving input from user
println("you name is ", name) # showing output to user

?exit # retuns help documentation on the exit function. Functions are typed without parenthesis
apropos("natural log") # returns functions whose description contains the string "natural log"

; # if you type ; you immidiately switch to shell mode
; ls # in shell mode you can type shell commands

# Julia and mathematics
1_000_000 / 1_000 # you can use _ as a number separator
planck_length = 1.61619997e-34 # to use scientific notation, just type "e" (or "E") and don't add any spaces

*(2,3,4) # does the same as 2 * 3 * 4

pi # some mathematical constants are inbuilt
Base.MathConstants.golden # golden ratio
Base.MathConstants.e # exponential

2 + 3 - 4 * 5 / 6 % 7 # All the usual operators are available
((2 + 3) - ((4 * 5) / 6) % 7) # the precedence of the operators is 
:(2 + 3 - 4 * 5 / 6 % 7) # If you want to check the precedence of operators, enclose the expression in :( and )

x=2 
2x + 4 # Multiplication is usually written *, but this can be omitted when multiplying a variable by a number literal

2^3 # power
10%4 # remainder

666//444 # To make rational numbers, use two slashes (//)

4 / 2 
2 \ 4 # There's also reverse division "\", so that x/y = y\x

# The standard arithmetic operators also have special updating versions, which you can use to update variables quickly:
x=5
x+=11
x-=3
*=
/=
\=
%=
^=

# Element-wise operatorsfor arrays
[2,4] .* [10, 20]

3/2 # returns 1.5, which is floating point ans
div(3,2) # returns 1, which is integer ans

# For big calculations
2^64 # oops
big(2)^64 # better
2^big(64) # equally better

x=10 # variable
x==10 # To test equality, you should use the == operator or isequal() function. 

a, b = 5, 3 # can also assign multiple variables at the same time


Julia replaces the \sqrt with a square root symbol
Some other examples:
\pi 	π
\Gamma 	Γ
\mercury 	☿
\degree 	°
\cdot 	⋅
\in 	∈ 


# Maths functions
sin(pi / 2)
log(12)
hypot(3, 4)
# norm() function (after loading via "using LinearAlgebra") returns the "p"-norm of a vector or the operator norm of a matrix
divrem(13, 3) # returns the division and the remainder

# Random numbers
rand() # gets one random Float64 between 0 and 1 
rand(2, 2) # an array of Float64s with dimensions 2, 2
rand(Bool, (2,2)) # rand(type, 2, 2) – an array of values of this type with dims 2, 2
rand(0:10, 6) # rand(range, dims) – array of numbers in a range (including both ends) with specified dimensions

# Random numbers in a distribution
randn(100) # randn() gives you one random number in a normal distribution with mean 0 and standard deviation 1. randn(n) gives you n such numbers

# Installing a package
import Pkg
Pkg.add("Plots")

# you can plot this
using Plots; gr()
histogram(randn(500), nbins=50)

# Seeding the random number generator
using Random
Random.seed!(10);
rand(0:10, 6)

# Simple keyboard input
function areaofcircle() 
    print("What's the radius?")
    r = parse(Float64, readline(stdin))
    print("a circle with radius $r has an area of:")
    println(π * r^2)
end
# call the function
areaofcircle()


##############################################################################
################################  arrays / tuples   ##########################
##############################################################################

# Arrays can be used for storing lists, vectors, tables, and matrices. 
# An array is an ordered collection of elements. 
# It's often indicated with square brackets and comma-separated items.
# You can create arrays that are full or empty, and 
# arrays that hold values of different types or restricted to values of a specific type. 
# Julia arrays are 'column-major'. This means that you read down the columns

# Creating arrays by initializing
arr_Int64 = [1, 2, 3, 4, 5]
arr_Float64 = [1, 2, 3, 4.0, 5]
arr_String = ["this", "is", "an", "array", "of", "strings"]
arr_Function = [sin, cos, tan]
arr_Any = [1, "2", 3.0, sin, pi] # It's possible to create arrays with elements of different types

# Creating uninitialized arrays using Array{type}(dims)
# random-looking numbers are a reminder that you've created an uninitialized array but haven't filled it with any sensible information
array = Array{Int64}(undef, 5)
array3 = Array{Int64}(undef, 2, 2, 2) # array of 3 dimentions

# Creating empty arrays
b = Int64[]
b = String[]
b = Float64[]

# Creating 2-d arrays
arr_2d = [1 2 3 4] # If you leave out the commas when defining an array, you can create 2D arrays quickly. Here's a single row, multi-column array: 
arr_2d = [1 2 3 4 ; 5 6 7 8] # you can add another row using ;

# Row and column vectors
col_vector = [1, 2, 3, 4, 5]
row_vector = [1 2 3 4 5]

[[1, 2, 3], [4, 5, 6]] # 2 rows x 3 cols
[[1, 2, 3] [4, 5, 6]]  # 3 rows x 2 cols

# Constructor functions
Vector(undef, 5) # aliases for uninitialized one dimensional arrays
Matrix(undef, 5, 5) # aliases for uninitialized two dimensional arrays; matrix is filled column by column

# Creating arrays using range objects
a = 1:10 # creates a range variable with 10 elements from 1 to 10
collect(a) # collect displays a range variable 
[a...] # instead of collect, you could use the ellipsis (...) operator (three periods) after the last element
for n in 1:10 print(n," ") end # can be used to run a for loop
collect(1:2:10) # start:step:stop
collect(4:-1:1) # To go down instead of up, you have to use a negative step value

# More range objects
range(1, length=12, stop=100) # Julia calculates the missing pieces for you by combining the values for the keywords step(), length(), and stop()
exp10.(range(2.0, stop=3.0, length=5)) # For logarithmic ranges (sometimes called 'log space'), you can use simple range objects and then broadcast the exp10 function (10^x) to every element of the range
step(range(1, length=10, stop=100)) # Use step() on a range object to find out what the step size is

# Chaining functions
1:10 |> collect

# Using comprehensions and generators to create arrays
[n^2 for n in 1:5] # a 1-d array
[r * c for r in 1:5, c in 1:5] # a 2-d array
[i^2 for i=1:10  if i != 5] # You can add an if test at the end to filter (keep) values that pass a test
# Generator functions
collect(x^2 for x in 1:10)
collect(x^2 for x in 1:10 if x != 1)
# The advantage of generator expressions is that they generate values when needed, rather than build an array to hold them first. 

# create arrays with specific contents
zeros(2, 3) # zeros(Int64, 3, 5)
ones(2, 3)
rand(2, 3) # rand(1:6, 3, 3)
# randn(m, n) creates an m-row by n-column matrix full of normally-distributed random numbers with mean 0 and standard deviation 1
trues(3, 4) # falses()
fill(42, 9) # to create an array with a specific value, i.e. an array of repeating duplicates
fill("hi", 2, 2)
# Fill an existing array
a = zeros(10)
fill!(a, 42) # the exclamation mark (!) or "bang" is to warn you that you're about to change the contents of an existing array (a useful indication that's adopted throughout Julia).

reshape([1, 2, 3, 4, 5, 6, 7, 8], 2, 4) # create a simple array and then change its shape
reshape(range(0, stop=100, length=30), 10, 3) # result is a 10 by 3 array featuring evenly-spaced numbers between 0 and 100. 
repeat([1, 2, 3], 2, 3) # repeat(A, n, m), the source array is repeated by n times in the first dimension (rows), and m times in the second (columns)
repeat([1, 2], inner = [2, 3])
repeat([1, 2], outer = [2, 3])
repeat([1 2; 3 4], inner=(2, 1), outer=(1, 3))

# Array Constructor - Each element is set to 'undefined' — #undef
# You can use Vector as an alias for Array
Array{Int}[] # empty array
Array{Int64}(undef, 6) # 1-d array
Array[[1, 2], [3,4]] # 2-d array
Array[1:3, 4:6] # 2-d array
Array{String}(undef, 2, 3, 4) # 3-d array

# ADD ELEMENTS
a = Array[[1, 2], [3,4]]
push!(a, [5,6]) # The push!() function pushes another item onto the back of an array
pushfirst!(a, 0) # To add an item at the front
splice() # To insert an element into an array at a given index
splice!(a, 4:5, 4:6) # insert, at position 4:5, the range of numbers 4:6
L = ['a','b','f']; splice!(L, 3:2, ['c','d','e']) # insert c, d, e between b and f

# REMOVE ELEMENTS
splice!(a,5); # If you don't supply a replacement, you can also use splice!() can remove elements and move the rest of them along
pop!(a) # To remove the last item
popfirst!(a)

b = similar(a) # Copying array dimensions using similar(). array dimensions are copied, but the values aren't

# Accessing arrays
# 1-d
a[5] # 5th element
a[end] # last element
a[end-1] # second last element
# 2-d
a = [[1, 2] [3,4]]
a[2,2] # element at row-2 x col-2
a[:,2] # all elements of col-2
getindex(a, 2,2) # same as a[2,2]

# Elementwise and vectorized operations
a / 100 # every element of the new array is the original divided by 100. These operations operate elementwise

n1 = 1:6;
n2 = 2:7;
n1 .* n2; # if two arrays are to be multiplied then we just add a . before the mathematical operator to signify elementwise
# the first element of the result is what you get by multiplying the first elements of the two arrays, and so on

# How function works on individual variables
f(a, b) = a * b
a=10;b=20;print(f(a,b))

# How function can be applied elementwise to arrays
n1 = 1:6;
n2 = 2:7;
print(f.(n1, n2))

max(), min() # return the largest value from arguments supplied to it
maximum(), minimum() # return the largest value from an array

a[a .== 0] .= 11; # test each value for being equal to 0, then set only those elements to 11

# Finding items in arrays
a = 1:10
3 in a
# findall(), findfirst(), findnext(), findprev() and findlast() — that you can use to get the index or indices of array cells that match a specific value, or pass a test
# findmax() finds the maximum element and returns it and its index in a tuple
# argmax() to return just the index
# Functions such as sum(), prod(), mean(), middle(), do what you would expect

# sum(), mean(), and prod() also let you supply functions: the function is applied to each element and then the results are summed/mean-ed/prod-ded
sum(sqrt, 1:10)  # the sum of the square roots of the first 10 integers

# Finding out about an array
ndims(a) # returns the number of dimensions, i.e. 1 for a vector, 2 for a table, and so on
size(a) # returns the row and column count of the array, in the form of a tuple
length(a) # tells you how many elements the array contains
count(!iszero, a) # tells you how many times a particular value occurs. !iszero helps to count how many non-zero items are there

1:10 |> diff # returns array of length-1, with difference between consecutive elements

union() # builds a new array that's the union or combination of two or more arrays. The operation removes duplicates, and the result contains a single version of each element: 
odds = collect(1:2:10); evens = collect(2:2:10); union(odds, evens)

intersect() # returns a new array that's the intersection of two or more arrays. The result contains one occurrence of each element, but only if it occurs in every array: 
intersect(1:10, 5:15)

setdiff() # finds the difference between two arrays, i.e. the elements that are in the first array but not the second: 
setdiff(1:15, 5:20)

filter(isodd, 1:10) # filter() finds and keeps elements if they pass a test. Here, we're using the isodd() function
count(isodd, 1:100) # counts the number of elements that satisfy the condition
any(isodd, 1:100) # tells you whether any of the elements satisfy the condition
all(isodd, filter(isodd, 1:100)) # tells you if all of the elements satisfy the condition


Pkg.add("Combinatorics") # (do this just once)
using Combinatorics
collect(combinations(a, 3)) # combinations() finds all the possible combinations of elements in an array: you can specify how many elements in each combination
length(permutations(a)) # permutations() generates all permutations. There are a lot — in practice you probably won't need to use collect() to collect the items into an array

# Additional functions
resize!() # change the length of a Vector
append!() # push a second collection at the back of the first one
prepend!() # insert elements at the beginning of the first Vector
empty!(a) # remove all elements
rotr90(a) # make a copy of an array rotated 90 degrees clockwise

# MATRIX operations
A * B # multiply (*), assuming the dimensions are compatible, so m1 * m2 is possible if last(size(m1)) == first(size(m2))
A / B # division
A \ B # back division
A + 1 # you can add, subtract, multiply, and divide a matrix and a scalar

# Joining arrays and matrices
# hcat() keeps the first dimension and extends (joins) in the second, vcat() keeps the second dimension and extends the first
# example - if A and B are two 3x4 arrays
hcat(A, B) # makes a new array that still has 3 rows, but extends/joins the columns to make 8 in total
vcat(A, B) # makes a new array that keeps the 4 columns, but extends to 6 rows

vec() # flattens a matrix into a vector, turning it into a (what some call a 'column') vector


##############################################################################
################################  types  #####################################
##############################################################################

Data elements come in different shapes and sizes, which are called types. 
Types are organized in a tree
supertype(Number) # returns the node above
subtypes(Number) # returns the nodes below
sizeof() # tells you how many bytes an item of this type occupies
# If you want to know how big a number you can fit into a particular type
typemax(Int64)
typemin(Int32)

# There are over 340 types in the base Julia system. You can investigate the type hierarchy with the following function:
 function showtypetree(T, level=0)
     println("\t" ^ level, T)
     for t in subtypes(T)
         showtypetree(t, level+1)
     end
 end
 showtypetree(Number)

#this function gets a number, and returns the same number plus one
function plus_one(n::Number) # uses the :: syntax, which means "is of type"
   return n + 1
end

# Concrete and abstract types
# The types that can have subtypes (e.g. Any, Number) are called abstract types
# The types that can have instances are called concrete types. These types cannot have any subtypes.

# Concrete types can be primitive (or basic), and complex (or composite)
primitive types:
    the basic integer and float types (signed and unsigned): Int8, UInt8, Int16, UInt16, Int32, UInt32, Int64, UInt64, Int128, UInt128, Float16, Float32, and Float64
    more advanced numeric types: BigFloat, BigInt
    Boolean and character types: Bool and Char
    Text string types: String
composite type is Rational, used to represent fractions. It is composed of two pieces, a numerator and a denominator, both integers (of type Int)


# Creating your own types
# abstract type
abstract type MyAbstractType end # By default, the type you create is a direct subtype of Any
abstract type MyAbstractType2 <: Number end # the new abstract type is a subtype of Number
# concrete type
# define the data type
mutable struct student <: Any
   name
   age::Int
end
# initialize a variable of that data type
x=student("vivek", 30)
# use the variable
x.name
x.age


##############################################################################
################################  flow control  ##############################
##############################################################################

# ternary and compound expressions
x = 1
x > 3 ? "yes" : "no"

# Boolean switching expressions
isodd(1000003) && @warn("That's odd!")
isodd(1000004) || @warn("That's odd!")

# if elseif else end - conditional evaluation
name = "Julia"
if name == "Julia"
   println("I like Julia")
elseif name == "Python"
   println("I like Python.")
   println("But I prefer Julia.")
else
   println("I don't know what I like")
end

# for end - iterative evaluation
# use the global keyword to define a variable that outlasts the loop
for i in 1:10
    z = i
    println("z is $z")
end

# Some sample for loop statements for different data types
for color in ["red", "green", "blue"] # an array
for letter in "julia" # a string
for element in (1, 2, 4, 8, 16, 32) # a tuple
for i in Dict("A"=>1, "B"=>2) # a dictionary
for i in Set(["a", "e", "a", "e", "i", "o", "i", "o", "u"])

# continue to skip the rest of the code inside the loop and start the loop again with the next value. 

# Nested for Loops
for x in 1:10
    for y in 1:10
        @show (x, y) # @show macro prints out the names of things and their values.
        if y % 3 == 0
           break
        end
    end
 end

# list comprehensions
[i^2 for i in 1:10]
[(r,c) for r in 1:5, c in 1:2] # two iterators in a comprehension
# Generator expressions - generator expressions can be used to produce values from iterating a variable
sum(x^2 for x in 1:10)
# Enumerating arrays
m = rand(0:9, 3, 3)
[i for i in enumerate(m)]
# Zipping arrays
for i in zip(0:10, 100:110, 200:210)
    println(i)
end
# Iterable objects
ro = 0:2:100
[i for i in ro]


# while end - iterative conditional evaluation
x=0
while x < 4
    println(x)
    global x += 1
end

x=0
while true
    println(x)
    x += 1
    x >= 4 && break # breaks out of the loop
end

# try catch error throw exception handling
try
    <statement-that-might-cause-an-error>;
catch e # error gets caught if it happens
    println("caught an error: $e") # show the error if you want to
end
println("but we can continue with execution...")

try
    a=10 # no error 
catch e
    print(e)
end

try
    la-la-la # undefined variable error
catch e
    print(e)
end

# do blocks


##############################################################################
################################  functions  #################################
##############################################################################

# A function is a collected group of instructions that can return one or more values, possibly based on the input arguments. 

# Single expression functions
f(x) = x * x
g(x, y) = sqrt(x^2 + y^2)

# Functions with multiple expressions
function say_hello(name) 
    println("hello ", name)
end
say_hello("vivek")

# return value
function add_numbers(a,b)
    return a+b
end
add_numbers(2,3)

# return multiple values
function add_multiply_numbers(a, b=10) # we can supply default values as well
    return(a+b, a*b)
end
add_multiply_numbers(2,3)
add_multiply_numbers(2)

# supplying variable number of arguments
function show_args(args...)
    for arg in args
        println(arg," ")
    end
end
show_args(10,20,25,35,50)

# Anonymous functions — functions with no name 
map((x,y,z) -> x + y + z, [1,2,3], [4, 5, 6], [7, 8, 9])

# Map - If you already have a function and an array, you can call the function for each element of the array by using map()
a=1:10;
map(sin, a) # map() returns a new array but if you call map!() , you modify the contents of the original array

# The map() function collects the results of some function working on each and every element of an iterable object, such as an array of numbers. 
map(+, 1:10)

# The reduce() function does a similar job, but after every element has been seen and processed by the function, only one is left. The function should take two arguments and return one.
reduce(+, 1:10)


##############################################################################
################################  dict and sets  #############################
##############################################################################

dict = Dict("a" => 1, "b" => 2, "c" => 3)
dict = Dict{String,Integer}("a"=>1, "b" => 2) # If you know the types of the keys and values in advance, you can specify them after the Dict keyword, in curly braces
# looking things up
dict["a"]
values(dict) # to retrieve all values
keys(dict) # to retrieve all keys
# these can be useful for iterating
for k in keys(dict)
for (key, value) in dict

merge(d1, d2) # merge() function which can merge two dictionaries
findmin(d1) # find the minimum value in a dictionary, and return the value, and its key
filter((k, v) -> k == 1, d1)

# sort dict - you can use the SortedDict data type from the DataStructures.jl package
Pkg.add("DataStructures")
import DataStructures
dict = DataStructures.SortedDict("b" => 2, "c" => 3, "d" => 4, "e" => 5, "f" => 6)

# Sets - A set is a collection of elements, just like an array or dictionary, with no duplicated elements. 
colors = Set{String}(["red","green","blue","yellow"])
push!(colors, "black")  # You can use push!() to add elements to a set

union(colors, rainbow) # The union of two sets is the set of everything that is in one or the other sets
intersect(colors, rainbow) # The intersection of two sets is the set that contains every element that belongs to both sets
setdiff(colors, rainbow) # The difference between two sets is the set of elements that are in the first set, but not in the second


##############################################################################
################################  str and char  ##############################
##############################################################################

"this is a string"

# double quotes and dollar signs need to be preceded (escaped) with a backslash
"""this is "a" string with double quotes""" # triple double quotes can be used to store strings with double quotes in them

# special strings
r" " indicates a regular expression
v" " indicates a version string
b" " indicates a byte literal
raw" " indicates a raw string that doesn't do interpolation

# string interpolation - use the results of Julia expressions inside strings.
x = 42
"The value of x is $(x)." # "The value of x is 42."

# Substrings - To extract a smaller string from a string, use getindex(s, range) or s[range] syntax
str ="a load of characters"
str[3:6] # "load"
str[3:end-6] # "load of char"

isascii(str) # functions tests whether a string is ASCII or contains Unicode characters

length(str) # to find the length of a string
lastindex(str) # to find index of last char of string

for char in s  # iterate through a string
    print(char, "_")
end

# Get index of all char in a string
for i in eachindex(str)
    @show su[i]
end

# Splitting and joining strings
"s" * "t"  # can stick strings together (a process often called concatenation) using the multiply (*) operator
string("s", "t")

"s" ^ 18  # can 'multiply' strings, you can also raise them to a power

split("You know my methods, Watson.") # by default splits on space
split("You know my methods, Watson.", 'W') # splits on the char W
# If you want to split a string into separate single-character strings, use the empty string ("") 

split("You know my methods, Watson.", r"a|e|i|o|u", false) # splits string on the char that matches any of the vowels
# false makes sure that empty strings are not returned

join(split(s, r"a|e|i|o|u", false), "aiou") # You can join the elements of a split string in array form using join()

# Converting between numbers and strings
a = BigInt(2)^200 
a=string(a) # convert number to string
parse(BigInt, a) # convert strings to numbers

# Finding and replacing things inside strings
s = "My dear Frodo";
in('M', s) # true
occursin("Fro", s) # true
findfirst("My", s) # 1:2
replace(s, "Frodo" => "Frodo Baggins")
uppercase(s)


# There are lots of functions for testing and changing strings:
    length(str) length of string
    sizeof(str) length/size
    startswith(strA, strB) does strA start with strB?
    endswith(strA, strB) does strA end with strB?
    occursin(strA, strB) does strA occur in strB?
    all(isletter, str) is str entirely letters?
    all(isnumeric, str) is str entirely number characters?
    isascii(str) is str ASCII?
    all(iscntrl, str) is str entirely control characters?
    all(isdigit, str) is str 0-9?
    all(ispunct, str) does str consist of punctuation?
    all(isspace, str) is str whitespace characters?
    all(isuppercase, str) is str uppercase?
    all(islowercase, str) is str entirely lowercase?
    all(isxdigit, str) is str entirely hexadecimal digits?
    uppercase(str) return a copy of str converted to uppercase
    lowercase(str) return a copy of str converted to lowercase
    titlecase(str) return copy of str with the first character of each word converted to uppercase
    uppercasefirst(str) return copy of str with first character converted to uppercase
    lowercasefirst(str) return copy of str with first character converted to lowercase
    chop(str) return a copy with the last character removed
    chomp(str) return a copy with the last character removed only if it's a newline


##############################################################################
################################  text files  ################################
##############################################################################

# A simple application of a dictionary is to count how many times each word appears in a piece of text.
f = open("sherlock-holmes-canon.txt")
wordlist = String[]
for line in eachline(f)
    words = split(line, r"\W")
    map(w -> push!(wordlist, lowercase(w)), words)
end
filter!(!isempty, wordlist)
close(f)
wordcounts = Dict{String,Int64}() # To store the words and the word counts, we'll create a dictionary
# To build the dictionary, loop through the list of words, and use get() to look up the current tally, if any. 
# If the word has already been seen, the count can be increased. 
# If the word hasn't been seen before, the fall-back third argument of get() ensures that the absence doesn't cause an error, and 1 is stored instead
for word in wordlist
    wordcounts[word]=get(wordcounts, word, 0) + 1
end
wordcounts["watson"] # Now you can look up words in the wordcounts dictionary and find out how many times they appear
# Dictionaries aren't sorted, but you can use the collect() and keys() functions on the dictionary to collect the keys and then sort them. 
# In a loop you can work through the dictionary in alphabetical order
for i in sort(collect(keys(wordcounts)))
    println("$i, $(wordcounts[i])")
end
# But how do you find out the most common words? 
# One way is to use collect() to convert the dictionary to an array of tuples, and then to sort the array by looking at the last value of each tuple
sort(collect(wordcounts), by = tuple -> last(tuple), rev=true)
# To see only the top 20 words
sort(collect(wordcounts), by = tuple -> last(tuple), rev=true)[1:20]
# In a similar way, you can use the filter() function to find, for example, all words that start with "k" and occur less than four times
filter(tuple -> startswith(first(tuple), "k") && last(tuple) < 4, collect(wordcounts))


# Read a text files
f = "/tmp/adventures-of-sherlock-holmes.txt"
text = read(f, String);


# Lets see how to read write in an organized way
f = open("sherlock-holmes.txt") # To read text from a file, first obtain a file handle: 
close(f) # When you've finished with the file, you should close the connection

# If you use the following then you dont need to close
# The open file is automatically closed when this block finishes
open("sherlock-holmes.txt") do file
    # do stuff with the open file
end


# These functions will be useful for working with filenames:
    cd(path) changes the current directory
    pwd() get the current working directory
    readdir(path) returns a lists of the contents of a named directory, or the current directory,
    abspath(path) adds the current directory's path to a filename to make an absolute pathname
    joinpath(str, str, ...) assembles a pathname from pieces
    isdir(path) tells you whether the path is a directory
    splitdir(path) - split a path into a tuple of the directory name and file name.
    splitdrive(path) - on Windows, split a path into the drive letter part and the path part. On Unix systems, the first component is always the empty string.
    splitext(path) - if the last component of a path contains a dot, split the path into everything before the dot and everything including and after the dot. Otherwise, return a tuple of the argument unmodified and the empty string.
    expanduser(path) - replace a tilde character at the start of a path with the current user's home directory.
    normpath(path) - normalize a path, removing "." and ".." entries.
    realpath(path) - canonicalize a path by expanding symbolic links and removing "." and ".." entries.
    homedir() - current user's home directory.
    dirname(path) - get the directory part of a path.
    basename(path)- get the file name part of a path.


##############################################################################
################################  date / time  ###############################
##############################################################################

# There are three main datatypes available:
    A Dates.Time object represents a precise moment of time in a day. It doesn't say anything about the day of the week, or the year, though. It's accurate to a nanosecond.
    A Dates.Date object represents just a date: no time zones, no daylight saving issues, etc... It's accurate to, well, a day.
    A Dates.DateTime object is a combination of a date and a time of day, and so it specifies an exact moment in time. It's accurate to a millisecond or so.

using Dates
import Dates # on of these is ok

Dates.Time(Dates.now()) # a Dates.Time object
Dates.Date(1997,3,15)   # a Dates.Date object
Dates.DateTime(1918,11,11,11,11,11) # a Dates.DateTime object
Dates.today() # returns a Date object for the current date
Dates.now() # function returns a DateTime object for the current instant in time
Dates.now(Dates.UTC)

Dates.year
Dates.month
Dates.day
Dates.minute
Dates.hour
Dates.second

Dates.dayofweek
Dates.dayname
Dates.yearmonth
Dates.yearmonthday
Dates.isleapyear
Dates.daysofweekinmonth
Dates.monthname
Dates.monthday
Dates.dayofweekofmonth

Dates.today() - Dates.Date(1997,3,15) # returns difference in number of days
Dates.today() - Dates.Month(6) # date 6 months ago 

# Date formatting
Dates.Date("Fri, 15 Jun 2018", "e, d u y")

y  Year digit eg yyyy => 2015, yy => 15
m  Month digit eg m => 3 or 03
u  Month name eg Jan
U  Month name eg January
e  Day of week eg Tue
E  Day of week eg Tuesday
d  Day eg 3 or 03
H  Hour digit eg HH => 00
M  Minute digit eg MM => 00
S  Second digit eg S => 00
s  Millisecond digit eg .000

# UNIX TIME
time() # function, used without arguments, returns the Unix time value of the current second
Libc.strftime(time()) # ("string format time") function, which lives in the Libc module, converts a number of seconds in Unix time to a more readable form

strptime() # function takes a format string and a date string, and returns a TmStruct expression. This can then be converted to a Unix time value by passing it to time()
time(Libc.strptime("%Y-%m-%d","2014-10-1"))
Libc.strftime(time(Libc.strptime("%Y-%m-%d","2014-10-1")))

unix2datetime() # function, which converts a Unix time value to a date/time object
Dates.unix2datetime(time())

# @elapsed macro returns the number of seconds an expression took to evaluate
function test(n)
    for i in 1:n
        x = sin(rand())
    end
end
@elapsed test(100000000)



##############################################################################
################################  plotting  ##################################
##############################################################################


##############################################################################
################################  metaprogramming  ###########################
##############################################################################


##############################################################################
################################  modules / packages  ########################
##############################################################################


##############################################################################
################################  dataframes  ################################
##############################################################################

import Pkg

Pkg.add("CSV")
Pkg.add("DataFrames") # Julia DataFrames package is an alternative to Python's Pandas package

Pkg.add("DataFramesMeta") # Julia-only packages Query.jl and DataFramesMeta.jl can also be used with DataFrames
Pkg.add("Query")

Pkg.add("Pandas") # but can be used with Pandas using the Pandas.jl wrapper package

Pkg.add("RDatasets") # contains a number of famous datasets

# Loading data into DataFrames
# option 1 - copy/paste data
import DataFrames
anscombe = DataFrame( # copy/paste several rows of data, convert them to an array,
 [10  10  10  8   8.04   9.14  7.46   6.58;    
  8   8   8   8   6.95   8.14  6.77   5.76;   
  13  13  13  8   7.58   8.74  12.74  7.71;   
  9   9   9   8   8.81   8.77  7.11   8.84;   
  11  11  11  8   8.33   9.26  7.81   8.47;   
  14  14  14  8   9.96   8.1   8.84   7.04;   
  6   6   6   8   7.24   6.13  6.08   5.25;   
  4   4   4   19  4.26   3.1   5.39   12.5;   
  12  12  12  8   10.84  9.13  8.15   5.56;   
  7   7   7   8   4.82   7.26  6.42   7.91;   
  5   5   5   8   5.68   4.74  5.73   6.89], :auto); 
rename!(anscombe, [Symbol.(:X, 1:4); Symbol.(:Y, 1:4)]) # rename the column names

# option 2 - collected datasets from the RDatasets package
import RDatasets
anscombe = dataset("datasets","anscombe")

# option 3 - Empty DataFrames
df = DataFrame(A = 1:6, B = 100:105) # by providing the information about rows, and column names, in arrays

df = DataFrame(Name=String[],  # create a completely empty DataFrame by supplying the column names and define their types
    Width=Float64[], 
    Height=Float64[], 
    Mass=Float64[], 
    Volume=Float64[])

df = vcat(df, DataFrame(Name="Test", Width=1.0, Height=10.0, Mass=3.0, Volume=5.0)) # Add rows to a dataframe

# Basics
typeof(anscombe)

https://en.wikibooks.org/wiki/Introducing_Julia/DataFrames

