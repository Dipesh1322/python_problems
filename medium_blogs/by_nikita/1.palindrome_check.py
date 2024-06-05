# check wether a string is a palindrome or not

def isPalindrome(a):
	reverse_a = a[::-1]
	if a == reverse_a:
		return True
	else:
		return False

name = "malayalam"
print(isPalindrome(name))

my_name = "dipesh"
print(isPalindrome(my_name))


# brute force approach

def isPali(_str):
	str_lst = [i for i in _str]
	print(f"str_lst:{str_lst}")
	str_lst.reverse()
	print(f"str_lst after reverse:{str_lst}")
	reverse_str = ""
	for i in str_lst:
		reverse_str += i
	print(f"reverse_str:{reverse_str}")
	
	if _str == reverse_str:
		return True
	else:
		return False

print(isPali(name))
print(isPali(my_name))