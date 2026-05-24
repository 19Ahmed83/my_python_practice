text = ["Python", "Java", "Rust", "Go", "C", "Ruby", "C++"]
result = list(filter(lambda x: len(x) > 3, text))
print(result)