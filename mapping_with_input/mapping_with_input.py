def mapping():
    names = []
    numbers = []

    while len(names) < 5:
        names_input = input("Enter name: ")
        numbers_input = input("Enter number: ")

        names.append(names_input)
        numbers.append(numbers_input)
    
    result = dict(zip(names, numbers))
    return result 

if __name__ == "__main__":
    print(mapping())    
