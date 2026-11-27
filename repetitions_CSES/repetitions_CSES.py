s = input("")

def fnc(s):
    count_prev = 1
    max_count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count_prev += 1
            max_count = max(max_count, count_prev)
        else:
            count_prev = 1
    return max_count        

if __name__ == "__main__":
    print(fnc(s))    