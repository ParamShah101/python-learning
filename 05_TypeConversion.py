# =================================================================
# Python Type Conversion
#
# Type conversion is the process of converting a value from one data type to another.
# Python has several built-in functions for type conversion, such as int(), float(), str(), etc.
# =================================================================

# 1. Initial Variable
# -----------------------------------------------------------------
# We start with an integer variable.
print("--- 1. Initial Variable ---")
intVariable = 15
print(f"Original Variable: {intVariable}, Type: {type(intVariable)}")
print("-" * 40)


# =================================================================
# 2. Integer to Float Conversion
#
# We convert the integer variable to a float.
# =================================================================
print("--- 2. Integer to Float Conversion ---")
floatVariable = float(intVariable)
print(f"Converted to Float: {floatVariable}, Type: {type(floatVariable)}")
print("-" * 40)


# =================================================================
# 3. Float to Complex Conversion
#
# We convert the float variable to a complex number.
# =================================================================
print("--- 3. Float to Complex Conversion ---")
complexVariable = complex(floatVariable)
print(f"Converted to Complex: {complexVariable}, Type: {type(complexVariable)}")
print("-" * 40)


# =================================================================
# 4. Explicit Type Casting
#
# We can also explicitly convert between types using casting functions.
# =================================================================
print("--- 4. Explicit Type Casting ---")

# Float to Integer
float_val = 9.8
int_val_from_float = int(float_val)
print(f"Float '{float_val}' to Integer: {int_val_from_float}, Type: {type(int_val_from_float)}")

# Integer to String
int_val = 100
str_val_from_int = str(int_val)
print(f"Integer '{int_val}' to String: '{str_val_from_int}', Type: {type(str_val_from_int)}")

# String to Integer
str_val_int = "123"
int_val_from_str = int(str_val_int)
print(f"String '{str_val_int}' to Integer: {int_val_from_str}, Type: {type(int_val_from_str)}")

# String to Float
str_val_float = "45.67"
float_val_from_str = float(str_val_float)
print(f"String '{str_val_float}' to Float: {float_val_from_str}, Type: {type(float_val_from_str)}")

print("-" * 40)

# Simple Way :- Conversion will do automatically And In Casting we have to explicitly define it

