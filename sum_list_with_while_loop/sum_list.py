def main(numbers):
    i = 0
    total = 0
    while i < len(numbers):
        total += numbers[i]
        i += 1
    return total

if __name__ == "__main__":
    print(main([5, 1, 6, 3, 7]))     