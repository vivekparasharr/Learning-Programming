
# Three ways of displaying content to user
p 'Hello World !!!'

puts 'Hello World !!!'

print 'Hello World !!!'

# Showing data stored in variables to user
my_name = "Vivek"
puts "Hello #{my_name}"

# This is a comment

=begin
    this is a comment
    block
    i can write as many
    lines of comment i want
=end

# Variables and Types
=begin
There are three main types of variable:
1. Strings (a collection of symbols inside speech marks)
2. Booleans (true or false)
3. Numbers (numeric values)
=end
    
aString = "I'm a string!" 
aBoolean = true 
aNumber = 42
puts "string: #{aString} \nboolean: #{aBoolean} \nnumber: #{aNumber}"


# Basic Math
a = 5
b = 2
puts "sum: #{a+b}\
    \ndifference: #{a-b}
    \nmultiplication: #{a*b}
    \ndivision: #{a/b}
    \nmodulo: #{a%b}
    \nexponent: #{a**b}"

# String manipulation
# You can use single quotes or double quotes for strings - either one is acceptable.
myFirstString = 'I am a string!' #single quotes
mySecondString = "Me too!" #double quotes
"Hi!".length #is 3
"Hi!".reverse #is !iH
"Hi!".upcase #is HI!
"Hi!".downcase #is hi!
# You can also use many methods at once. They are solved from left to right.
"Hi!".downcase.reverse #is !ih
# If you want to check if one string contains another string, you can use .include?.
"Happy Birthday!".include?("Happy")

# Arrays allow you to group multiple values together in a list. Each value in an array is referred to as an "element".
myArray = []  # an empty array
myOtherArray = [1, 2, 3]  # an array with three elements
# In order to add to or change elements in an array, you can refer to an element by number.
myOtherArray[3] = 4



# Hashes and Symbols (similar to dictionary in python)
# Just like arrays, hashes allow you to store multiple values together. However, while arrays store values with a numerical index, hashes store information using key-value pairs. Each piece of information in the hash has a unique label, and you can use that label to access the value.
# To create a hash, use Hash.new, or myHash={}. For example:
myHash=Hash.new()
myHash["Key"]="value"
myHash["Key2"]="value2"
# or
myHash={
    "Key" => "value",
    "Key2" => "value2"
}
# You can access a value like so:
puts myHash["Key"] # puts value

# Instead of using a string as a key, you can also use a symbol, like this:
myHash=Hash.new()
myHash[:Key]="value"
myHash[:Key2]="value2"
# or
myHash={
    Key: "value",
    Key2: "value2",
}
# You can access a value like so:
puts myHash[:Key] # puts "value"


=begin
Ruby is a perfect Object Oriented Programming Language. The features of the object-oriented programming language include −
a. Data Encapsulation
b. Data Abstraction
c. Polymorphism
d. Inheritance
An object-oriented program involves classes and objects. A class is the blueprint from which individual objects are created. In object-oriented terms, we say that your bicycle is an instance of the class of objects known as bicycles.

Ruby provides four types of variables:
a. Local Variables − Local variables are the variables that are defined in a method. Local variables are not available outside the method. You will see more details about method in subsequent chapter. Local variables begin with a lowercase letter or _.
b. Instance Variables − Instance variables are available across methods for any particular instance or object. That means that instance variables change from object to object. Instance variables are preceded by the at sign (@) followed by the variable name.
c. Class Variables − Class variables are available across different objects. A class variable belongs to the class and is a characteristic of a class. They are preceded by the sign @@ and are followed by the variable name.
d. Global Variables − Class variables are not available across classes. If you want to have a single variable, which is available across classes, you need to define a global variable. The global variables are always preceded by the dollar sign ($).
=end
# Example - A class Vehicle can be defined as −
Class Vehicle {
   Number no_of_wheels
   Number horsepower
   Characters type_of_tank
   Number Capacity
   Function speeding {
   }
   Function driving {
   }
   Function halting {
   }
}

# Creating Objects in Ruby using new Method
vehicle1 = Vehicle.new
# Custom Method to Create Ruby Objects - for this you need to declare the method initialize at the time of the class creation. The initialize method is a special type of method, which will be executed when the new method of the class is called with parameters.
class Customer
    @@no_of_customers = 0
    def initialize(id, name, addr)
       @cust_id = id
       @cust_name = name
       @cust_addr = addr
    end
 end
# Now, you can create objects as follows −
cust1 = Customer.new("1", "Vivek", "Somewhere on the, Internet")



# Conditional Statements
# Conditionals are used to add branching logic to your programs; they allow you to include complex behaviour that only occurs under specific conditions.

# if condition is an expression that can be checked for truth. If the expression evaluates to true, then the code within the block is executed.
if condition
    something to be done
end

# You can combine if with the keyword else. This lets you execute one block of code if the condition is true, and a different block if it is false. 
# The else block will only be executed if the if block doesn't run, so they will never both be executed.
if condition
    something to be done
else
    something to be done if the condition evaluates to false
end
    
# When you want more than two options, you can use elsif. This allows you to add more conditions to be checked.
# Here is if/elsif/else statement syntax:
# Still only one of the code blocks will be run, because the statement only executes the code in the first applicable block; Once a condition has been satisfied, the whole statement ends. 
if condition
  something to be done
elsif different condition
  something else to be done
else
  another different thing to be done
end

# Following is an actual example of an if statement with both an elsif and an else.
booleanOne = true
randomCode = "Hi!"
if booleanOne
  puts "I will be printed!"
elsif randomCode.length>=1
  puts "Even though the above code is true, I won't be executed because the earlier if statement was true!"
else
  puts "I won't be printed because the if statement was executed!"
end

# Executes code if conditional is false. If the conditional is true, code specified in the else clause is executed.
unless condition
    # thing to be done if the condition is false
else
    # else is optional
    # thing to be done if the condition is true
end

# Ruby if modifier - executes code if the conditional is true.
code if condition
# Ruby unless modifier - Executes code if conditional is false.
code unless conditional

# Ruby case Statement
case expr0
when expr1, expr2
   stmt1
when expr3, expr4
   stmt2
else
   stmt3
end
# is basically similar to the following −
if expr1 === expr0 || expr2 === expr0
   stmt1
elsif expr3 === expr0 || expr4 === expr0
   stmt2
else
   stmt3
end
# Example of case statement
$age =  5
case $age
when 0 .. 2
   puts "i will not be printed"
when 3 .. 6
   puts "i will be printed"
when 7 .. 12
   puts "i will not be printed"
when 13 .. 18
   puts "youth"
else
   puts "i will not be printed"
end



# Looping - For, While, and Until
# For Syntax - Executes code once for each element in expression.
for variable [, variable ...] in expression [do]
   code
end
# Example
for i in 0..5
    puts "Value of local variable is #{i}"
end


# while - Executes code while conditional is true. A while loop's conditional is separated from code by the reserved word do, a newline, backslash \, or a semicolon ;
# Syntax
while conditional [do]
    code
end
# Example 
a=1
b=5
while a<=b
    puts "run #{a}" 
    a=a+1 
end

# Ruby while modifier - Executes code while conditional is true.
code while condition
# or
begin # If a while modifier follows a begin statement with no rescue or ensure clauses, code is executed once before conditional is evaluated.
    code 
end while conditional

# until - Executes code while conditional is false. An until statement's conditional is separated from code by the reserved word do, a newline, or a semicolon.
until conditional [do]
    code
end  
# Example
$i = 0
$num = 5
until $i > $num  do
   puts("Inside the loop i = #$i" )
   $i +=1;
end

# Ruby until modifier - Executes code while conditional is false.
code until conditional
# or 
begin # If an until modifier follows a begin statement with no rescue or ensure clauses, code is executed once before conditional is evaluated.
    code
end until conditional

# break - Terminates the most internal loop. Terminates a method with an associated block if called within the block (with the method returning nil).
# next - Jumps to the next iteration of the most internal loop. Terminates execution of a block if called within a block (with yield or call returning nil).
# redo - Restarts this iteration of the most internal loop, without checking loop condition. Restarts yield or call if called within a block.
# retry - If retry appears in rescue clause of begin expression, restart from the beginning of the begin body.
# retry - If retry appears in the iterator, the block, or the body of the for expression, restarts the invocation of the iterator call. Arguments to the iterator is re-evaluated.


# Methods are reuseable sections of code that perform specific tasks in our program. Using methods means that we can write simpler, more easily readable code. 
def methodname
    # method code here
end

# Methods With Parameters
def laugh(number)
    puts "haha " * number
end
# Using method - calling method as follows prints "haha" 5 times on the screen
laugh(5)
# You can also call laugh without paranthesis
laugh 5

# We can set default values for the parameters, which will be used if method is called without passing the required parameters
def method_name (var1 = value1, var2 = value2)
    expr..
end

# return statement in ruby is used to return one or more values from a Ruby Method.
return
# or
return 12
# or
return 1,2,3

# Variable Number of Parameters
def sample (*test)
    puts "The number of parameters is #{test.length}"
    for i in 0...test.length
       puts "The parameters are #{test[i]}"
    end
end
sample "Zara", "6", "F"
sample "Mac", "36", "M", "MCA"


# Class method - Let us see how a class method is declared and accessed
class Accounts
    def reading_charge
    end
    def Accounts.return_date
    end
end
# You can access this class method directly as follows
Accounts.return_date

