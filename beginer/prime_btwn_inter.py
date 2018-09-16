N=int(input("Enter N value: "))
Q=int(input("Enter Q value: "))
for i in range(N,Q+1):
    if i>1:
        for n in range (2,i):
            if i%n==0:
                break
        else:
            print i
