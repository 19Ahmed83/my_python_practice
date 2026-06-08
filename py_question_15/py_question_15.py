def func():
    count = {}
    text = input("Enter your text: ")

    words_list = text.split()
    for word in words_list:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count            

print(func())