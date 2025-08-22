# =================================================================
# Python String Methods
#
# Strings in Python have many built-in methods for manipulation.
# =================================================================

print("--- String Methods in Python ---")

# 1. Upper and Lower
text = "Hello World"
print("Original:", text)
print("Upper:", text.upper())      # Convert to UPPERCASE
print("Lower:", text.lower())      # Convert to lowercase
print("-" * 40)

# 2. Strip (remove spaces)
text_with_spaces = "   Python   "
print("Before strip:", repr(text_with_spaces))
print("After strip:", repr(text_with_spaces.strip()))
print("-" * 40)

# 3. Replace
msg = "I like Java"
print("Before replace:", msg)
print("After replace:", msg.replace("Java", "Python"))
print("-" * 40)

# 4. Split and Join
sentence = "Python is fun"
words = sentence.split()  # split by spaces
print("Split into list:", words)
print("Join with '-':", "-".join(words))
print("-" * 40)

# 5. Find and Index
quote = "Learn Python, Learn Coding"
print("Find 'Python':", quote.find("Python"))   # returns index
print("Index of 'Coding':", quote.index("Coding"))  # raises error if not found
print("-" * 40)

# 6. Startswith / Endswith
filename = "report.pdf"
print("Starts with 'rep':", filename.startswith("rep"))
print("Ends with '.pdf':", filename.endswith(".pdf"))
print("-" * 40)

# 7. Count
msg = "banana"
print("Count of 'a':", msg.count("a"))
print("-" * 40)

# 8. Title and Capitalize
title_text = "welcome to python"
print("Title:", title_text.title())       # Capitalize each word
print("Capitalize:", title_text.capitalize())  # Only first letter
print("-" * 40)

# 9. isdigit(), isalpha(), isalnum()
print("'12345'.isdigit():", "12345".isdigit())
print("'abc'.isalpha():", "abc".isalpha())
print("'abc123'.isalnum():", "abc123".isalnum())
print("-" * 40)

# 10. Formatting (f-strings or format method)
name = "Alice"
age = 25
print(f"My name is {name}, I am {age} years old.")
print("My name is {}, I am {} years old.".format(name, age))
print("-" * 40)


# 11. String Concation

a = "Hello"
b = "World"

print(a + b) # HelloWorld

print(a,b) # Hello World