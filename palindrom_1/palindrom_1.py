n = int(input("Enter a number: "))
rev = 0
temp = n

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

if n == rev:
    print("Palindrome")

else:
    print("Not Palindrome")    