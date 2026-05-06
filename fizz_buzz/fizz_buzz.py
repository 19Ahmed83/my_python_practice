def fizzbuzz(n):
    lst = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            lst.append("fizz_buzz")
        elif i % 3 == 0:
            lst.append("fizz")
        elif i % 5 == 0:
            lst.append("buzz")
        else:
            lst.append(i)
    return lst

print(fizzbuzz(15))                    
