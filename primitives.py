print("Houston we have lift off!!!!")
# _ Numbers & Variables
# < Left is "location" or "thing" right is the VALUE
this_variable = 10
print(this_variable)
# output-> 10
print(type(this_variable))
# output-> <class 'int'>
float_num = 160.22
print(float_num)
# output-> 160.22
print(type(float_num))
# output-> <class 'float'>
# < Operators + - * /
# < addition, subtraction, multiplication, division respectively
print(3/2)
# output-> 1.5
# < // "floor division" operator
#? performs division. result is the quotient rounded down to the nearest integer
print(3//2)
# output-> 1
# < assignment operators shorthand, 
# < Perform math operation and assign variable value simultaneously
# < +=, -=, *=, /=
num = 4
num = num + 1
print(num)
# output-> 5
num += 1
print(num)
# output-> 6
# < combine with floor div operand
num //= 2
print(num)
# output-> 3
# < output-> 3.0 as simply /=

# _ Booleans
# < Assesses/represents the truthiness value of something
# < Operators <, >, <=, >=, ==, !=, is, is not, or, and
my_bool = True
print(my_bool)
# output -> True
print(type(my_bool))
# output-> <class 'bool'>
my_bool = this_variable
print(my_bool)
# output-> 10
# Example of python being dynamically typed
print(bool(5<2))
# output-> False
print(bool(5>2))
# output-> True
print(bool(5==2))
# output-> False
print(5 is 0)
# output-> False
print(5 is not 0)
# output-> True

# _ Strings
# < Any sequence of characters (letters, numerals, ~($/}\#, etc...) 
# < enclosed in single, double or triple quotes
a_string = "hello"
print(a_string)

# output-> hello
print(type(a_string))
# output-> <class 'str'>
char = 'a'
print(len(char),type(char))
# output-> 1 <class 'str'>
print(a_string*3)
# output-> hellohellohello
mystring = 'this is a "string"?'
response = 'Yes'
print(mystring,response)
# output-> this is a "string"? Yes
print(mystring+response)
# output-> this is a "string"?Yes
print(mystring+" "+response)
# output-> this is a "string"? Yes
# < When using multiple quotes in one string 
# < start with singles inside and move outwards matching starting and closing quotes
# ! "Hello World', 'hello World" <- wrong
single_quotes = 'this is camerons food'
double_quotes = "this is camerons food"
# ! 'this is cameron's food' <- wrong
# output-> SyntaxError: unterminated string literal (detected at line 57)
# < escaping
print('this is cameron\'s food')
apostrophe = "this is cameron's food"
print(apostrophe)
# output-> this is cameron's food
# ! "this is "Cameron's" food" <- wrong
multiple_quotes = "this is 'cameron's' food"
print(multiple_quotes)
# output-> this is 'cameron's' food
multiple_quotes = """this is "cameron's" food"""
print(multiple_quotes)
# # output-> this is "cameron's" food

# _ Reserved keywords 
# > as multi-line string
"""
False    class    finally  is       return
None     continue for      lambda   try
True     def      from     nonlocal while
and      del      global   not      with
as       elif     if       or       yield
assert   else     import   pass     break    
except   in       raise
"""

# _ Type Casting
# < to change a value's data type from one type to another
int_to_float = float(35)
print(int_to_float)
# output-> 35.0
print(type(int_to_float))
# output-> <class 'float'>
float_to_int = int(44.9)
print(float_to_int)
# output-> 44
print(type(float_to_int))
# output-> <class 'int'>
# < str() ->  int() it has to be a number to treat it as a number
#! print(int(a_string))
# output-> ValueError: invalid literal for int() with base 10: 'hello'
# < Numbers can be changed to strings
print(str(float_num))
# output-> 160.22
print(type(str(float_num)))
# output-> <class 'str'>

# _ String Interpolation (foramtted strings)
string1 = "Cameron is "
string2 = " years old"
age = "35"
print(string1)
# output-> Cameron is 
print(string1+str(age)+string2)
# output-> Cameron is 35 years old
print(int(age)+1)
# output-> 36
# < Great for debugging
print(f"string1: {string1}")
# output-> string1: Cameron is
print(f"I think '{string1}' {age} years old")
# output-> I think 'Cameron is ' 35 years old

# * Most languages have something like this(outdated)
first_name = "Cameron"
last_name = "Smith"
age = 34
# < Correct :
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
#! Incorrect: 
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))