# Approach-1:
def largest_element(arr):
	arr.sort()
	return arr[-1]


lst = [10, 5, 8, 20, 3]
print(largest_element(lst))


# Approach-2:
def largest_element(arr):
	largest = arr[0]
	for i in arr:
		if i>largest:
			largest = i
	return largest


lst = [10, 5, 8, 20, 3]
print(largest_element(lst))