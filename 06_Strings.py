# =================================================================
# Python Strings
#
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".
# =================================================================

# 1. String Declaration
# -----------------------------------------------------------------
# Strings can be enclosed in single or double quotes.
print("--- 1. String Declaration ---")
print('Hello')
print("Heyy")
print("-" * 40)


# =================================================================
# 2. Assign String to a Variable
# -----------------------------------------------------------------
# You can assign a string to a variable.
print("--- 2. Assign String to a Variable ---")
a = "Python"
print(f"The value of variable 'a' is: {a}")
print("-" * 40)


# =================================================================
# 3. Multiline Strings
# -----------------------------------------------------------------
# You can assign a multiline string to a variable by using three quotes.
print("--- 3. Multiline Strings ---")
value = """
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
"""
print("Multiline String:")
print(value)
print("-" * 40)


# =================================================================
# 4. String Indexing
# -----------------------------------------------------------------
# Strings are arrays of bytes representing unicode characters.
# Square brackets can be used to access elements of the string.
print("--- 4. String Indexing ---")
name = "Python"
print(f"String: {name}")
print(f"First character (name[0]): {name[0]}")
print(f"Third to last character (name[-2]): {name[-2]}")
print("-" * 40)


# =================================================================
# 5. Looping Through a String
# -----------------------------------------------------------------
# Since strings are arrays, you can loop through the characters in a string.
print("--- 5. Looping Through a String ---")
print("Looping through 'apple':")
for x in "apple":
    print(x)
print("-" * 40)


# =================================================================
# 6. Checking String Membership
# -----------------------------------------------------------------
# To check if a certain phrase or character is present in a string, we can use the 'in' keyword.
print("--- 6. Checking String Membership ---")
txt = "The best things in life are free!"
print(f"Text: '{txt}'")
is_free_present = "free" in txt
print(f"Is 'free' in the text? {is_free_present}")
print("-" * 40)

# =================================================================
# 7. String Slicing
# -----------------------------------------------------------------
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
print("--- 7. String Slicing ---")
word = "Hello World"
print(f"Original String: '{word}'")

# Slice from index 2 to 5 (5 is not included)
print(f"Slice from index 2 to 5 (word[2:5]): '{word[2:5]}'")

# Slice from index 2 to the end
print(f"Slice from index 2 to end (word[2:]): '{word[2:]}'")

# Slice from the beginning to index 8 (8 is not included)
print(f"Slice from beginning to index 8 (word[:8]): '{word[:8]}'")

# Negative indexing: Slice from index -5 to -2 (-2 is not included)
print(f"Slice from index -5 to -2 (word[-5:-2]): '{word[-5:-2]}'")
print("-" * 40)