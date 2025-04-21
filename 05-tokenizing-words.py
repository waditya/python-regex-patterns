import re

text = "Hello! How are you today 06/12/2023? I hope everything is going well. Have a great day."

word_pattern = r"\b(?![\d.!?])\w+\b"
character_pattern = r"\b(?![\w])\d"
words = re.findall(word_pattern, text)

print(words)
print(re.findall(character_pattern, text))