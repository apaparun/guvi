n = int(input("Enter a number: "))
if n<=100:
    for i in range(2, int(n/2)):
        if n%i==0:
            print "Not a prime number"
            break
    else:
        print "Prime number"
else:
    print "Enter numbers less than 1000"
