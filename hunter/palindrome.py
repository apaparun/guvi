class Stack:
    def __init__(s):
        s.items = [] 
    def is_empty(s):
        return s.items == [] 
    def push(s, data):
        s.items.append(data) 
    def pop(s):
        return s.items.pop()
    def size(s):
        return len(S.items)
strn = Stack()
a = input()
if (len(a)<=100000):
    for char in a:
        strn.push(char)
        rev_text = ''
    while not strn.is_empty():
        rev_text = rev_text + strn.pop()
    if (a == rev_text):
        print('YES')
    else:
        print('NO')
else:
    print("invalid")
