# Approach-1:
def reverse_string(string):
    return string[::-1]

# Test the function
text = "Hello, World!"
reversed_text = reverse_string(text)
print(reversed_text)


# Approach-2:
def reverse_string(string):
	str_lst = [i for i in string]
	str_lst.reverse()
	reverse_str = "".join(str_lst)
	return reverse_str

# Test the function
text = "Hello, World!"
reversed_text = reverse_string(text)
print(reversed_text)


# Approach-3:
def reverse_string(original_list):
	reverse_list = [original_list[len(original_list) - i] for i in range(1, len(original_list)+1)]
	a = ""
	for i in reverse_list:
		a+=i
	return a

# Test the function
text = "Hello, World!"
reversed_text = reverse_string(text)
print(reversed_text)