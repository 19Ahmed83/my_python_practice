def check_password():
    password = input("Enter your password: ")
    
    while password:
        try:
            if password == "123":
                print("Ok")
                break

            else:
                password = input("Enter correct password: ")
                
        except ValueError:
            print("Incorrect")
            continue

    return password

if __name__ == "__main__":
    check_password()        

