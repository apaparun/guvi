a=str(raw_input("Enter the string:"))
if (len(a)<=100000):
    a=a[::-1]
    print a
else:
    print ("Enter string value less than 100000")
