def main():
    name = greeting(str)

    if "hello" in name:
        print("$0")
    elif name[0] == "h" and name != "hello":
        print("$20")
    else:
        print("$100")        




def greeting(str):
    str = input("Enter your greetings: ")
    return str.lower()


main()