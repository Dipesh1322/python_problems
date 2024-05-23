# Approach 1:
def removeDuplicates(array):
	b = []
	for i in array:
		if i not in b:
			b.append(i)

	return b


lst = [1,2,3,2,"dipesh",4,6,4,109,2,"dipesh","dippi"]
print(removeDuplicates(lst))


# Approach 2:
def removeDuplicatesAgain(array):
	b = []
	[b.append(i) for i in array if i not in b]
	return b


lst = [1,2,3,2,"dipesh",4,6,4,109,2,"dipesh","dippi"]
print(removeDuplicatesAgain(lst))