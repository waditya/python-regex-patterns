import re

text = "This sentence includes !@#$% special characters *&^."

clean_text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

print(clean_text)