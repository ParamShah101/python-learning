# =================================================================
# Python Variables
#
# Variables are containers for storing data values.
# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.
# =================================================================

# 1. Variable Declaration and Assignment
# -----------------------------------------------------------------
# Variables do not need to be declared with any particular type,
# and can even change type after they have been set.

print("--- 1. Variable Declaration and Assignment ---")
x = 5           # x is of type int
name = "Sara"   # name is now of type str
print("Value of x:", x)
print("Value of name:", name)
print("-" * 40)


# =================================================================
# 2. Type Casting
#
# If you want to specify the data type of a variable,
# this can be done with casting.
# =================================================================

print("--- 2. Type Casting ---")
a = str(3)    # a will be '3'
b = int(3)    # b will be 3
c = float(3)  # c will be 3.0

print("a (str(3)):", a)
print("b (int(3)):", b)
print("c (float(3)):", c)
print("-" * 40)


# =================================================================
# 3. Getting the Variable Type
#
# You can get the data type of a variable with the type() function.
# =================================================================

print("--- 3. Getting the Variable Type ---")
print("Type of a:", type(a))
print("Type of b:", type(b))
print("Type of c:", type(c))
print("-" * 40)


# =================================================================
# 4. Case-Sensitivity
#
# Variable names are case-sensitive.
# =================================================================

print("--- 4. Case-Sensitivity ---")
p = "Hello"
P = "World"
# In this example, 'p' and 'P' are two different variables.
print("Value of p:", p)
print("Value of P:", P)
print("-" * 40)

# =================================================================
# 5. Variable Naming Conventions
#
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).
# Rules for Python variables:
# - A variable name must start with a letter or the underscore character
# - A variable name cannot start with a number
# - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# - Variable names are case-sensitive (age, Age and AGE are three different variables)
# =================================================================

print("--- 5. Variable Naming Conventions ---")
# Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

print("This section is for demonstrating naming conventions. No output to display.")
print("-" * 40)

# Illegal variable names (will cause a syntax error if uncommented):
# 2myvar = "John"
# my-var = "John"
# my var = "John"


# =================================================================
# 6. Assign Multiple Values
#
# Python allows you to assign values to multiple variables in one line.
# =================================================================

print("--- 6. Assign Multiple Values ---")
x, y, z = "Orange", "Banana", "Cherry"
print("x:", x)
print("y:", y)
print("z:", z)

# You can also assign the same value to multiple variables in one line.
a = b = c = "Apple"
print("a:", a)
print("b:", b)
print("c:", c)
print("-" * 40)

# =================================================================
# 7. Unpack a Collection
#
# If you have a collection of values in a list, tuple etc.
# Python allows you to extract the values into variables.
# This is called unpacking.
# =================================================================
print("--- 7. Unpack a Collection ---")

fruits = ["apple", "banana", "cherry"]
x,y,z = fruits
print("X :", x)


# =================================================================
# 8. Global Variable
#
# Variables that are created outside a function is called Global Variable.
# =================================================================

print("--- 8. Global Variable ---")

word = "Awesome"

def myfunc():
    word = "Fantastic"
    print("Python is ", word)

myfunc()

print("Python is ", word)



# Global Variable

word1 = "Awesome"

def myfunc1():
    global word1
    word1 = "Fantastic"
    print("Python is ", word1)

myfunc1()

print("Python is ", word1)