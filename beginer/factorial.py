n=int(raw_input())
facto=1
if (n<0):
	print("factorial does not exist")
else:
	for i in range(1,n+1):
		facto=facto*i
	print (facto)
