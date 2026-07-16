s = int(input("Enter time in seconds "))

h = s // 3600
remaining_seconds  = s % 3600 
m = remaining_seconds  // 60
sec = remaining_seconds  % 60

print(" the time is " , h,"hr",m,"min",sec,"seconds")