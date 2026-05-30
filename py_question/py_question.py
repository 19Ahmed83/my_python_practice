def func(x, y = None):
    if y is None:
        y = [1]
    y.extend(x)
    return y

if __name__ == "__main__":
    print(func([0], [2, 4, 5]))

# output: [2, 4, 5, 0]    