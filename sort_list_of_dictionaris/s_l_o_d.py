users = [{"name": "Ali", "age": 25}, {"name": "Zara", "age": 22}, {"name": "Sam", "age": 30}]
sorted_users = sorted(users, key = lambda x: x["age"])
print(sorted_users)