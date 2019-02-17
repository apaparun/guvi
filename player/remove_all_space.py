while True:
    try:
        strn=input()
        break
    except:
    	print("invalid")
    	break
if len(strn)<=100000 :
    ans=strn.replace(" ","")
    print(ans)
else:
    print("invalid")
