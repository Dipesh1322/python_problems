def factorial(num):
    try:
        num = int(num)
        if num <0:
            return f"{num} is negative. Please input a positive whole integer."
        elif num==0:
            return 1
        return num*factorial(num-1)
    except:
        return f"{num} is not a positive whole integer!!"

number = input("Please input a positive whole integer:")
print(factorial(number))
