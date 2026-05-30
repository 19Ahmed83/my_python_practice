def func():
    a, *b = ["John", "Peter", "Bob"]
    names = b
    return "Peter" in [names]

if __name__ == "__main__":
    print(func())

#output False    