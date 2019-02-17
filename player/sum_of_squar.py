n=int(raw_input())
t=0
while(n>0):
    d=n%10
    t=t+(d**2)
    n=n//10
print t
