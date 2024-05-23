def commonLetters(my_name,your_name):
    lst = [i.lower() for i in my_name]
    common_letters = []
    for i in your_name:
        if i.lower() in lst:
            common_letters.append(i)
    common_lst = []
    [common_lst.append(i) for i in common_letters if i not in common_lst]
    return common_lst

my_name = "Dipesh"
your_name = "Deeksha"
print(commonLetters(my_name,your_name))
