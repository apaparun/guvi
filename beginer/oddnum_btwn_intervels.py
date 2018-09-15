N=int(input("Enter N value: "))
Q=int(input("Enter Q value: "))
if N and Q <=100000:
    for i in range(N,Q+1):
        if i%2!=0:
            print i 
else:
    print "Enter numbers less than 100000"
