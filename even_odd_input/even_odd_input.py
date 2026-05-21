def even_odd():
    numbers = []
    count_even = 0
    count_odd = 0
    while len(numbers) < 5:
        try:
            date = list(map(int, input("Enter number").split()))
            for el in date:
                if len(numbers) < 5:
                    numbers.append(el)
                    if el % 2 == 0:
                        count_even += 1
                    else:
                        count_odd += 1 
                        
        except ValueError:
            print("Enter integer number:")
        continue
    return count_even, count_odd     

if __name__ == "__main__":
    even, odd = even_odd()
    print(f"Even: {even}, odd: {odd}")        


