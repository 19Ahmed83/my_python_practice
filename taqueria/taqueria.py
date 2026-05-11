menu = {
    
    "Baj Taco": 4.25,
    "Burrito" : 7.50,
    "Bowl" : 8.50,
    "Nachos" : 11.0,
    "Quesadilla" : 8.50,
    "Super Burrito" : 8.50,
    "Super Quesadilla" : 9.50,
    "Taco" : 3.00,
    "Tortilla Salad" : 8.00

}

total_sum = 0

while True:
    try:
        item = input("Item: ")
        if item in menu:
            total_sum += menu[item]
            print(f"Total: ${total_sum:.2f}")
    except EOFError:
        print()
        break        