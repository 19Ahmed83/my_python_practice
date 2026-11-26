n = input("")

def max_num(n):
    a = {}
    
    for i in n:
        if i not in a:
            a[i] = 1
        else:
            a[i] += 1
    return max(a.values())             


if __name__ == "__main__":
    
    print(max_num(n)) 