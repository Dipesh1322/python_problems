# Approach-1
def commonLetters(my_name,your_name):
    lst = [i for i in my_name.lower()]
    common_letters = []
    for i in your_name.lower():
        if i in lst:
            common_letters.append(i)
    common_lst = []
    [common_lst.append(i) for i in common_letters if i not in common_lst]
    return common_lst

my_name = "Dipesh"
your_name = "Deeksha"
print(commonLetters(my_name,your_name))

# Approach-2
def commons(a,b):
    c= []
    for i in a.lower():
        if i in b.lower():
            c.append(i)
    return c
print(commons(my_name,your_name))

# Approach-3
def comms(a,b):
    c = [i for i in a.lower() if i in b.lower()]
    return c
print(comms(my_name,your_name))
