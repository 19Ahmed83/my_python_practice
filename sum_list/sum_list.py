def main(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

if __name__ == "__main__":
    print(main([1, 7, 0, 4]))     


def sum_list(numbers):
    i = 0
    total = 0
    while i < len(numbers):
        total += i
    return total        

if __name__ == "__main__":
    print(main([4, 7, 3, 5]))