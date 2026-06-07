from collections import Counter

text = "python is fun and python is powerful"
freq = Counter(text.split())
print(freq)