from collections import Counter

def main(arr):
    counts = Counter(arr)
    for el in sorted(counts):
        print(counts[el], el.upper())

if __name__ == "__main__":
    main(["banana", "apple", "orange", "banana"])        
        