def palindrome():
    text = input("Enter a number: ")
    return "Palindrome" if text == text[::-1] else "Not palindrome"

print(palindrome())