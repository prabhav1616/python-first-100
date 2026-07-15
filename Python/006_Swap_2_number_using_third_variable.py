a = int(input("Enter a single digit number "))
b = int(input("enter the second single digit number "))

temp = a
a = b 
b = temp

print("the number before swap ", b,a)
print("the number after swap ", a,b)