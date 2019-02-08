str=input()
if len(str)<=10000000:
    for i in range(0, len(str), 2):
        swap=''.join([str[i:i+2][::-1]])
        print(swap,end="")
else:
    print("invalid")
