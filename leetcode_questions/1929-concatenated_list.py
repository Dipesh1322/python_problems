def concatenated_list(array):
	lst_2 = []
	for i in array:
		lst_2.append(i)
	return lst_2 + array

def concatenated_list_method_1(array):
	lst_2 = [i for i in array]
	return lst_2 + array

def concatenated_list_method_2(array):
	lst_2 = [i for i in array]
	lst_2.extend(array)
	return lst_2

def concatenated_list_method_3(array):
	lst_2 = [i for i in array] + array
	return lst_2

def concatenated_list_method_4(array):
	return [i for i in array] + array

def concatenated_list_method_5(array):
	return array + array

lst = [1,2,3]
print(concatenated_list(lst))
print(concatenated_list_method_1(lst))
print(concatenated_list_method_2(lst))
print(concatenated_list_method_3(lst))
print(concatenated_list_method_4(lst))
print(concatenated_list_method_5(lst))