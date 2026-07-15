a = int(input("enter the first number "))
b = int(input("enter the second number "))
print("The numbers before swap : ",a,b)


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Before swap:", a, b)

a = a + b
b = a - b
a = a - b

print("After swap:", a, b)