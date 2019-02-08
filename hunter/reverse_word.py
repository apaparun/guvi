try:
    s=raw_input()
except:
    print "invalid"
    
x= s.split(" ")
for x in x:
    y= [x[::-1]]
    z=" ".join(y)
    print z,
