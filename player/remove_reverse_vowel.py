n=int(raw_input())
string=raw_input()
vowels = ('a', 'e', 'i', 'o', 'u')
if len(string)==n and 1<=len(string)<=1000000 :
	for x in string.lower():
		if x in vowels:
			string = string.replace(x, "")
	string = string[::-1]
	print string
else:
	print "invalid"
