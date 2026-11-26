n = int(input())
nums = list(map(int, input().split()))
def miss_number(n, nums):
    s = n * (n + 1) // 2
    return s - sum(nums)

print(miss_number(n, nums))


