import re

text = "The meeting will start at 14:30. Please be on time."

time_pattern = r"\b\d{2}:\d{2}\b"
times = re.findall(time_pattern, text)

print(times)