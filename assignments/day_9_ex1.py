# Write a program using function to find greatest of three numbers entered by 

def find_greatest_number(num1, num2, num3,):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
num3=int(input("Enter third number"))

result = find_greatest_number(num1, num2, num3)


print(f"The greatest number is {result}")
