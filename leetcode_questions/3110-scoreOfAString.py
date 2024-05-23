# Approach-1
def score(s):
    ord_lst = []
    abs_lst = []
    for i in range(len(s)):
        ord_lst.append(ord(s[i]))
    for i in range(len(ord_lst)):
        for j in range(i+1,len(ord_lst)):
                       abs_var = abs(ord_lst[i]-ord_lst[j])
                       abs_lst.append(abs_var)
                       break
    return sum(abs_lst)
s = 'hello'
print(score(s))

# Approach-2
def score(s):
    counter = 0
    for i in range(len(s)-1):
        counter += abs(ord(s[i])-ord(s[i+1]))
    return counter
print(score(s))
