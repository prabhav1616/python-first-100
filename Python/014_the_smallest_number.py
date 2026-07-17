#write a python program to check the smallest number among three numbers

a = int(input("Enter the first number "))
b = int(input("Enter the second number "))
c = int(input("Enter the third number "))


if a < b and a < c :
    print( a, " is the smallest number  ")
if b < a and b < c :
    print(b," is the smallest number ")
if c < a and c < b :
    print(c, " is the smallest number ")
    
# will it run if input is (5,5,3)
