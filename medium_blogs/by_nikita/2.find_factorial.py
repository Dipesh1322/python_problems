def factorial(num):
	if num == 0:
		return 1
	else:
		return num*factorial(num-1)

a = 4
print(factorial(a))

def factorial(a):
    if a == 0:
            return 1
    else:
            return a*factorial(a-1)

num = int(input("Type a natural number:"))
print(factorial(num))
