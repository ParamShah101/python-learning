# =================================================================
# Python Operators
#
# Operators are used to perform operations on variables and values.
# =================================================================

# 1. Arithmetic Operators
# -----------------------------------------------------------------
# Used with numeric values to perform common mathematical operations.
print("--- 1. Arithmetic Operators ---")
a = 10
b = 3
print(f"a = {a}, b = {b}")
print(f"Addition (a + b): {a + b}")          # 13
print(f"Subtraction (a - b): {a - b}")        # 7
print(f"Multiplication (a * b): {a * b}")      # 30
print(f"Division (a / b): {a / b}")            # 3.33...
print(f"Modulus (a % b): {a % b}")              # 1
print(f"Exponentiation (a ** b): {a ** b}")    # 1000
print(f"Floor Division (a // b): {a // b}")      # 3
print("-" * 40)


# =================================================================
# 2. Assignment Operators
# -----------------------------------------------------------------
# Used to assign values to variables.
print("--- 2. Assignment Operators ---")
x = 5
print(f"Initial x: {x}")
x += 3  # same as x = x + 3
print(f"x += 3: {x}")
x -= 2  # same as x = x - 2
print(f"x -= 2: {x}")
x *= 4  # same as x = x * 4
print(f"x *= 4: {x}")
x /= 3  # same as x = x / 3
print(f"x /= 3: {x}")
print("-" * 40)


# =================================================================
# 3. Comparison Operators
# -----------------------------------------------------------------
# Used to compare two values.
print("--- 3. Comparison Operators ---")
val1 = 10
val2 = 20
print(f"val1 = {val1}, val2 = {val2}")
print(f"Equal (val1 == val2): {val1 == val2}")            # False
print(f"Not Equal (val1 != val2): {val1 != val2}")          # True
print(f"Greater Than (val1 > val2): {val1 > val2}")        # False
print(f"Less Than (val1 < val2): {val1 < val2}")          # True
print(f"Greater or Equal (val1 >= val2): {val1 >= val2}") # False
print(f"Less or Equal (val1 <= val2): {val1 <= val2}")    # True
print("-" * 40)


# =================================================================
# 4. Logical Operators
# -----------------------------------------------------------------
# Used to combine conditional statements.
print("--- 4. Logical Operators ---")
p = True
q = False
print(f"p = {p}, q = {q}")
print(f"p and q: {p and q}")  # True if both are true
print(f"p or q: {p or q}")   # True if at least one is true
print(f"not p: {not p}")      # Inverts the boolean value
print("-" * 40)


# =================================================================
# 5. Identity Operators
# -----------------------------------------------------------------
# Used to compare the objects, not if they are equal, but if they are
# actually the same object, with the same memory location.
print("--- 5. Identity Operators ---")
list1 = ["apple", "banana"]
list2 = ["apple", "banana"]
list3 = list1
print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"list3: {list3}")
print(f"list1 is list3: {list1 is list3}")      # True, same object
print(f"list1 is list2: {list1 is list2}")      # False, different objects with same content
print(f"list1 is not list2: {list1 is not list2}")# True
print("-" * 40)


# =================================================================
# 6. Membership Operators
# -----------------------------------------------------------------
# Used to test if a sequence is presented in an object.
print("--- 6. Membership Operators ---")
fruits = ["apple", "banana", "cherry"]
print(f"fruits: {fruits}")
print(f"'banana' in fruits: {'banana' in fruits}")        # True
print(f"'grape' not in fruits: {'grape' not in fruits}")  # True
print("-" * 40)


# =================================================================
# 7. Bitwise Operators
# -----------------------------------------------------------------
# Used to compare (binary) numbers.
print("--- 7. Bitwise Operators ---")
num1 = 6  # 0110 in binary
num2 = 2  # 0010 in binary
print(f"num1 = {num1} (0110), num2 = {num2} (0010)")
print(f"AND (num1 & num2): {num1 & num2}")      # 2 (0010)
print(f"OR (num1 | num2): {num1 | num2}")       # 6 (0110)
print(f"XOR (num1 ^ num2): {num1 ^ num2}")      # 4 (0100)
print(f"NOT (~num1): {~num1}")                  # -7 (inverts all bits)
print(f"Left Shift (num1 << 1): {num1 << 1}") # 12 (1100)
print(f"Right Shift (num1 >> 1): {num1 >> 1}")# 3 (0011)
print("-" * 40)