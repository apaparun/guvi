def ComPrefix( a): 
    size = len(a)  
    if (size == 0): 
        return ""
    if (size == 1): 
        return a[0] 
    a.sort()
    end = min(len(a[0]), len(a[size - 1]))  
    i = 0
    while (i < end and a[0][i] == a[size - 1][i]): 
        i += 1
    pref = a[0][0: i] 
    return pref
if __name__ == "__main__": 
    t = int(input())
    arr=[]
    for i in range(t):
        arr_n = input()
        arr.append(arr_n)
    print(ComPrefix(arr)) 
