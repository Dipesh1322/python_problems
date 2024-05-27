# Approach-1 - Not a very good approach bacause uses a count function
def word_count(string):
	a = string.split()
	a = [i.lower() for i in a if i != '.']
	b = {}
	for i in a:
	    b[i] = a.count(i)
	print(b)

sentence = "Sheena loves eating apple and mango . Her sister also loves eating apple and mango . Go Mango ."
word_count(sentence)


# Approach-2 - Better approach because doesn't use in-built function, rather is more inclined towards logic
def count_words(line):
    a = line.split()
    a = [i.lower() for i in a if i!='.']
    b = {}
    for i in a:
        if i not in b:
            b[i] = 0
        b[i]+=1
    return b

print(count_words(sentence))