def complete_nums(numbers):
    n = max(numbers)
    seen = set(numbers)
    missing = []

    for i in range(1, n + 1):
        if i not in seen:
            missing.append(i)

    return missing

if __name__ == "__main__":
    print(complete_nums([3, 4, 2, 9, 5, 11]))        