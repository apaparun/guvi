while True:
    try:
        a,t=input().split()
        b=75
        a=int(a)
        t=int(t)
        break
    except:
        print("invalid")
        break
if(a==0):
    print(a)
elif(a<=5):
    d=b+t
    print(d)
else:
    c=75+8*(a-5)+t
    print(c)
