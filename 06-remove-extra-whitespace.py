import re

text = "This    sentence   has   extra   whitespaces."

clean_text = re.sub(r"\s+", " ", text)

print(clean_text)