def func(k, v, my_dict = {}):
    my_dict[k] = v
    return my_dict

dict_1 = func("mom", 48)
dict_2 = func("dad", 56)

print(dict_1)

#output {"mom": 48, "dad": 56}