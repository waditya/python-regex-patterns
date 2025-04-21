import re

html = "<h1>Welcome to the Regex World</h1><p>Enjoy the power of regex!</p>"

clean_text = re.sub(r"<.*?>", " ", html)

print(clean_text)