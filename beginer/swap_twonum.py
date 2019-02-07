a,b=input().split()
if len(a)<=100000:
	tem=a
	a=b
	b=tem
	print(a+" "+b)
else:
	print("invalid")
