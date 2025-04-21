import re

text = "The event will take place on 06-12-2023. Don't miss it!"

date_pattern = r"\b\d{2}-\d{2}-\d{4}\b"
dates = re.findall(date_pattern, text)

print(dates)