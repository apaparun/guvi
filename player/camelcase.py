s=raw_input()
if len(s)<=1000000:
    for x in s.split(' ' or '_'):
        cam=''.join(x.capitalize() or ' ' or '_' )
        print cam,
else:
    print "invalid"
