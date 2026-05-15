def main():
    while True:
        try:
            value = int(input("Enter x: "))
            print(f"You entered: {value}")
            break
        except ValueError:
            print("Error: Please enter correct x:")

if __name__ == "__main__":
    main()