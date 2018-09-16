U=int(input("Enter the starting number : "))
L=int(input("Enter the ending number : "))
for n in range(U,L+1):
    sum=0
    temp=n
    cube=len(str(n))

    while temp>0:
        dig=temp%10
        sum+=dig**cube
        temp//=10
    if sum==n:
        print n
