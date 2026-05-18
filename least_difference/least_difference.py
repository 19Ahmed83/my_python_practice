def least_difference(a, b, c):
    diff_1 = abs(a - b)
    diff_2 = abs(b - c)
    diff_3 = abs(a - c)
    return min(diff_1, diff_2, diff_3)

if __name__ == "__main__":
    print(least_difference(13, 3, 7))
