def frequency(arr):
    dict = {}
    for i in lst:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    return dict

lst = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
print(frequency(lst))