num = [1, 2, 3, 4, 5]
count_even = 0
count_odd = 0


for el in num:
    if el % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print(f"Number of even elements: {count_even}, number of odd elements: {count_odd} ")             
        