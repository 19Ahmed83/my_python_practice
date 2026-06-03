def func(k, v, my_dict = None):
    if my_dict is None:
        my_dict = {}
    my_dict[k] = v
    return my_dict

dict_1 = {"mom", 48}
dict_2 = {"dad", 56}
print(dict_1)   