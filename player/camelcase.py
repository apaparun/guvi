s=input()
for x in s.split(' ' or '_'):
    cam=''.join(x.capitalize() or ' ' or '_' )
    print(cam,end=" ")
