a=int(input("Enter the number: "))
x=a
y=0
while(a>0):
    k=a%10
    y=y*10+k
    a=a//10
if(x==y):
    print "yes"
else:
    print "no"
