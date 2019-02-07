str=input()
count=0
if len(str)<=1000:
    for i in str:
        if i.isdigit() :
            count=count+1
    print(count)
else:
    print("invalid")
