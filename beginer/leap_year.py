leap=int(raw_input("Enter the year: "))
if((leap%400 == 0) or ((leap%4 == 0) and (leap%100 != 0))):
    print("Leap year")
else:
    print("Not leap year")
    
