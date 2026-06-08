def func(text):
    count = {}
    for i in text:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count   

user_input = input("Enter your text: ")             
print(func(user_input))