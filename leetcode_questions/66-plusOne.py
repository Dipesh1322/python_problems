def plusOne(array):
	lst_str = [str(i) for i in array]
	str_to_int = int("".join(lst_str))
	plusOne_str = str(str_to_int + 1)
	plusOne = [int(i) for i in plusOne_str]
	return plusOne

lst = [1,2,3,9]
print(plusOne(lst))