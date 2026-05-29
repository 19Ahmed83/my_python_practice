def find_disappear_numbers(nums):
    n = len(nums)
    seen = set(nums)
    missing = []
    res = 0
    for i in range(1, n + 1):
        if i not in seen:
            missing.append(i)
            
            

    return missing

if __name__ == "__main__":
    print(find_disappear_numbers([1, 2, 3, 4, 7, 8, 9]))            