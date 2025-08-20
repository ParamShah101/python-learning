# In Python there are several built-in data types.

# =================================================================
# 1. Numbers
#
# There are three numeric types in Python:
# - int: Integer, a whole number, positive or negative, without decimals, of unlimited length.
# - float: Floating point number, a number, positive or negative, containing one or more decimals. Float can also be scientific numbers with an "e" to indicate the power of 10.z
# - complex: Complex numbers are written with a "j" as the imaginary part.
# =================================================================

print("--- 1. Numbers ---")
intVariableExample = 10
print(f"Integer Example: {intVariableExample}, Type: {type(intVariableExample)}")

floatVariableExample = 10.0
print(f"Float Example: {floatVariableExample}, Type: {type(floatVariableExample)}")

complexVariableExample = 10j
print(f"Complex Example: {complexVariableExample}, Type: {type(complexVariableExample)}")
print("-" * 40)


# =================================================================
# 2. String
#
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".
# =================================================================

print("--- 2. String ---")
stringVariableExample = "Hello"
print(f"String Example: '{stringVariableExample}', Type: {type(stringVariableExample)}")
print("-" * 40)


# =================================================================
# 3. Boolean
#
# Booleans represent one of two values: True or False.
# =================================================================

print("--- 3. Boolean ---")
booleanVariableExample = True
print(f"Boolean Example: {booleanVariableExample}, Type: {type(booleanVariableExample)}")
print("-" * 40)


# =================================================================
# 4. List
#
# Lists are used to store multiple items in a single variable.
# Lists are created using square brackets.
# List items are ordered, changeable, and allow duplicate values.
# =================================================================

print("--- 4. List ---")
listVariableExample = [1, 2, 3, 4, 5]
print(f"List Example: {listVariableExample}, Type: {type(listVariableExample)}")
print("-" * 40)


# =================================================================
# 5. Tuple
#
# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
# =================================================================

print("--- 5. Tuple ---")
tupleVariableExample = (1, 2, 3, 4, 5)
print(f"Tuple Example: {tupleVariableExample}, Type: {type(tupleVariableExample)}")
print("-" * 40)


# =================================================================
# 6. Set
#
# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# * Note: Set items are unchangeable, but you can remove items and add new items.
# Sets are written with curly brackets.
# =================================================================

print("--- 6. Set ---")
setVariableExample = {1, 2, 3, 4, 5}
print(f"Set Example: {setVariableExample}, Type: {type(setVariableExample)}")
print("-" * 40)


# =================================================================
# 7. Dictionary
#
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered**, changeable and does not allow duplicates.
# ** As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# Dictionaries are written with curly brackets, and have keys and values.
# =================================================================

print("--- 7. Dictionary ---")
dictionaryVariableExample = {"name": "John", "age": 30}
print(f"Dictionary Example: {dictionaryVariableExample}, Type: {type(dictionaryVariableExample)}")
print("-" * 40)


# ==================================================================
# 8. Python Boolean (Additional)

# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones
# ==================================================================