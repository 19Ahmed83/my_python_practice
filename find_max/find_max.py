 #find the maximum element in an array

lst = [3, 9, 15, 2, 8, 11, ]

def find_max(lst):
    max_el = lst[0]
    for el in lst:
        if el > max_el:
            max_el = el
    return max_el
print(find_max(lst))            
