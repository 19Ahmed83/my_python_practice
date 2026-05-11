arr = []

while True:
    try:
        item = input("")
        if item:
            arr.append(item)
    except EOFError:
        break

count = {}

for el in arr:
    if el in count:
        count[el] += 1
    else:
        count[el] = 1 
for el in sorted(set(arr)):
    print(count[el], el.upper())           