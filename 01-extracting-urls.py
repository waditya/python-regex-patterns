import re

text = "Visit my website at https://example.com or check out the latest news at http://news.example.com"

url_pattern = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"
urls = re.findall(url_pattern, text)

print(urls)