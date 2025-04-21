import re

html = '<a href="https://example.com">Visit our website</a>'

href_pattern = r'href="([^"]*)"'
href = re.search(href_pattern, html).group(1)

print(href)