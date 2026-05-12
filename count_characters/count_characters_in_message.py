from collections import Counter

message = "It was a bright cold day in April, and the clocks were striking thirteen. "

counts = {}
for i in message:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1 
print(counts)      

def main(message):
    counts = Counter(message)
    for el in counts:
        print(counts[el], el)

if __name__ == "__main__":

    main("It was a bright cold day in April, and the clocks were striking thirteen. ")        
