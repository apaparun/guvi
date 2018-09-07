vowel=('a','e','i','o','u')
conso=('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z')
var=raw_input("Enter the letter")
if var in vowel :
    print("vowel")
elif var in conso :
    print("consonant")
else:
    print("invalid")
