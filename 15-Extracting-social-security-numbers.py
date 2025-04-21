import re

text = "The SSN of John Doe is 123-45-6789."

ssn_pattern = r"\d{3}-\d{2}-\d{4}"
ssns = re.findall(ssn_pattern, text)

print(ssns)