a = int(input("Enter a single digit number "))
b = int(input("enter the second single digit number "))

temp = a
a = b 
b = temp

print("the number before swap ", b,a)
print("the number after swap ", a,b)

# or do this 

#print("Before swap:", a, b)

#temp = a
#a = b
#b = temp

#print("After swap:", a, b)