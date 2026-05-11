def main(arr):
    count = {}
    for el in arr:
        if el in count:
            count[el] += 1
        else:
            count[el] = 1
    for el in sorted(set(arr)):
        print(count[el], el.upper())

if __name__ == "__main__":
    main(["banana", "apple", "orange", "banana", "apple"])                