while True:
	try:
		n=int(raw_input())
		num=[]
		for i in range(n):
			num= list(map(int, raw_input().split()))
		break
	except:
		break
odd,eve=[],[]
for i in range(n):
    if i%3==0 and num[i]%3!=0:
        odd.append(num[i])
    elif i%3!=0 and num[i]%3==0:
        odd.append(num[i])
for k in odd:
	print k,
