import re

text = 'She said, "Life is short, enjoy every moment"'

quote_pattern = r'"([^"]*)"'
quotes = re.findall(quote_pattern, text)

print(quotes)