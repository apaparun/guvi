try:
    s=input()
except:
    print("invalid")
import re
ans=re.sub(" +"," ",s)
print(ans)
