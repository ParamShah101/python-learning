# =================================================================
# Python Escape Sequences
#
# Escape sequences are special characters that are used to represent
# characters in a string that would otherwise be difficult or
# impossible to type directly.
# =================================================================

print("--- Python Escape Sequences ---")

# 1. Double Quote (\")
# -----------------------------------------------------------------
# To include a double quote inside a string that is enclosed in
# double quotes, you need to escape it.
print("--- 1. Double Quote (\") ---")
text_with_quote = "I love to code in \"Python\""
print("String with escaped double quote:", text_with_quote)
print("-" * 40)


# =================================================================
# 2. New Line (\n)
#
# The '\n' character is used to insert a new line.
# =================================================================
print("--- 2. New Line (\\n) ---")
text_with_newline = "This is the first line.\nThis is the second line."
print("String with new line:")
print(text_with_newline)
print("-" * 40)


# =================================================================
# 3. Tab (\t)
#
# The '\t' character is used to insert a tab.
# =================================================================
print("--- 3. Tab (\\t) ---")
text_with_tab = "Column1\tColumn2\tColumn3"
print("String with tabs:")
print(text_with_tab)
print("-" * 40)


# =================================================================
# 4. Backslash (\\)
#
# To include a literal backslash, you need to escape it with another
# backslash.
# =================================================================
print("--- 4. Backslash (\\\\) ---")
text_with_backslash = "This is a backslash: \\"
print("String with a backslash:", text_with_backslash)
print("-" * 40)


# =================================================================
# 5. Single Quote (\')
#
# While you can use single quotes inside double-quoted strings
# without escaping, you need to escape them inside single-quoted strings.
# =================================================================
print("--- 5. Single Quote (\\') ---")
text_with_single_quote = 'He said, \'Hello!\''
print("String with escaped single quote:", text_with_single_quote)
print("-" * 40)