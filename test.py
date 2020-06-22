def gettype(s):
    n=0
    for i in s:
        try:
            x=int(i)
            n+=1
        except:
            n+=1
    return n

t=int(input())
for _ in range(t):
    s=input()
    print(type(s[0]),type(s[1]))