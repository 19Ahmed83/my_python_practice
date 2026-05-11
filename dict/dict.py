# arr = ["banana", "apple", "orange", "banana", ]

# count = {}
# for item in arr:
#     if item in count:
#         count[item] += 1
#     else:
#         count[item] = 1

# for item in sorted(set(arr)):        
#     print(count[item], item.upper())  
# 

def main(arr):
    count = {}
    for el in arr:
        if el in count:
            count[el] += 1
        else:
            count[el] = 1
    for el in sorted(set(arr)):
        print(count[el], el.upper())
        
if __name__ == "__main__":
    main(["banana", "apple", "banana", "orange", "banana"])               