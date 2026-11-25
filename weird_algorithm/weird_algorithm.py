n = int(input())

def w_algorithm(n):
    while n != 1:
        print(n, end = " ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    print(n)
w_algorithm(n)        