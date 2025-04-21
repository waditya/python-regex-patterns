import re

text = "This is is a test sentence to find duplicate duplicate words."

duplicate_pattern = r"\b(\w+)\b(?=.*\b\1\b)"
duplicates = re.findall(duplicate_pattern, text)

print(duplicates)


# Regex Breakdown

# Let’s deconstruct it:

# 1. \b(\w+)\b

# \b: Word boundary (ensures full word match).

# (\w+): Captures one or more word characters (letters, digits, underscore).

# So this part captures each individual word in the string.

# 2. (?=.*\b\1\b)

# This is a lookahead. It's saying:
# “After this word, there must be another occurrence of the same word somewhere later in the string.”

# .: Any character

# *: Zero or more characters

# \b\1\b: Matches the same word captured earlier (\1) as a whole word again.
                                                
# ---------------------------------

# How it works on the string:
# It moves through each word and:

# Captures it

# Then looks ahead in the string to see if that same word appears again

# If yes → match!

# Example:
# "This" → lookahead sees no "This" later → no match

# "is" → lookahead sees another "is" → match!

# "a" → not duplicated → skip

# "duplicate" → appears again → match!

# "words" → only once → skip

# ##Key Regex Concepts Used

# Concept	Explanation
# \b	    Word boundary
# (\w+)	    Capturing a word
# (?=...)	Lookahead — ensures something follows
# \1	    Backreference to the captured group (same word)