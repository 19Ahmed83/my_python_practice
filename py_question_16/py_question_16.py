def func():
    text = input("Enter your text: ")
    words = text.split()
    word_lengths = {}
    for word in words:
        word_lengths[word] = len(word)
    return word_lengths
print(func())    