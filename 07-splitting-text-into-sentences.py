import re

text = "Hello! How are you today? I hope everything is going well. Have a great day."

sentence_pattern = r"(.*?[.!?])"
sentences = re.findall(sentence_pattern, text)

print(sentences)