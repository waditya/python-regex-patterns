import re

text = "Just enjoying a #beautiful day with #friends in #nature"

hashtag_pattern = r"#\w+"
hashtags = re.findall(hashtag_pattern, text)

print(hashtags)