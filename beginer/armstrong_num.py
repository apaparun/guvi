n=int(input("Enter the number: "))
sum=0
temp=n
if n<=100000:
    while temp>0:
        dig=temp%10
        sum+=dig**3
        temp//=10
    if sum==n:
        print n,"is armsrtong number"
    else:
        print n,"is not an armstrong number"
else:
    print "Enter number less than 100000"
