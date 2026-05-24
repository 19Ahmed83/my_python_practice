numbers = [1, 2, 2, 3, 4, 4, 5]
unique = []
[unique.append(x) for x in numbers if x not in unique]
print(unique)