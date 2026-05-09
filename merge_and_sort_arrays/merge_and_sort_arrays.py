def merge_sort_arrays(arr_1, arr_2):
    result = sorted(arr_1 + arr_2)
    return result

print(merge_sort_arrays([1, 5, 3, 9], [7, 2, 6, 0]))