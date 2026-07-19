#write a program to check weather it is a leap year or not


year = int(input("Enter a year YYYY : "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) :
    print(year," is a leap year")
else: 
    print(year,"it is not a leap year")
    
    
    
    
    