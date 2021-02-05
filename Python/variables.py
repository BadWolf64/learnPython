# This is a comment
"""
This is a multiline comment.
"""

"""
VARIABLE NAMING 
    A variable name must start with a letter or the underscore character
    A variable name cannot start with a number
    A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    Variable names are case-sensitive (age, Age and AGE are three different variables)
"""

#Camel Case Variable naming
myVariableName = int(8)     #this is also an example of casting the variable type.

#Pascal Case Variable nameing (variables are case sensitive so this will not overwrite myVariableName)
MyVariableName = str(8)     #this is casting of type string

#Snake Case Variable naming
my_variable_name = float(8)

print(myVariableName)
print(MyVariableName)
print(my_variable_name)
print(type(myVariableName))
print(type(MyVariableName))
print(type(my_variable_name))

#Variables can be assinded in one line. 

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Can be assinged the same value in one line.

x = y = z = "Orange"
print(x)
print(y)
print(z)

#Can be unpacked 

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

"""
GLOBAL VARIABLES
    x in the below is a Global variable and is available to the function myfunc
    if you want to change a Global Variable inside of a function then you need to use the keyword. 
"""

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#Using the keyword to change a global variable inside of a function 

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

"""
DATA TYOE

    x = "Hello World"	str	
    x = 20	int	
    x = 20.5	float	
    x = 1j	complex	
    x = ["apple", "banana", "cherry"]	list	
    x = ("apple", "banana", "cherry")	tuple	
    x = range(6)	range	
    x = {"name" : "John", "age" : 36}	dict	
    x = {"apple", "banana", "cherry"}	set	
    x = frozenset({"apple", "banana", "cherry"})	frozenset	
    x = True	bool	
    x = b"Hello"	bytes	
    x = bytearray(5)	bytearray	
    x = memoryview(bytes(5))	memoryview
"""

"""
SETTING DATA TYPE WITH A CAST

    x = str("Hello World")	str	
    x = int(20)	int	
    x = float(20.5)	float	
    x = complex(1j)	complex	
    x = list(("apple", "banana", "cherry"))	list	
    x = tuple(("apple", "banana", "cherry"))	tuple	
    x = range(6)	range	
    x = dict(name="John", age=36)	dict	
    x = set(("apple", "banana", "cherry"))	set	
    x = frozenset(("apple", "banana", "cherry"))	frozenset	
    x = bool(5)	bool	
    x = bytes(5)	bytes	
    x = bytearray(5)	bytearray	
    x = memoryview(bytes(5))	memoryview
"""

