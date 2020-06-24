t=int(input())
def func(s):
    if not s[1].isnumeric():
        return 2
    else:
        for i in s[2:]:
            if not i.isnumeric():
                return 1
        return 2
def convert(c,s):
    if c==1:
        for i in range(1,len(s)):
            if not s[i].isnumeric():
                index = i
                break
        num = s[1:index]
        num2 = s[index+1:]
        num2 = int(num2)
        string = ""
        while num2>0:
            x=num2%(26)
            num2 = num2//(26)
            if x==0:
                x=26
                num2 = num2 -1
            o = chr(x+64)
            string = o+string
            i+=1
        print(string+num)
    else:
        index = 0
        for i in range(0,len(s)):
            if s[i].isnumeric():
                index = i
                break
        alpha = s[0:index]
        num = s[index:]
        l = len(alpha)
        num2=0
        for i in range(l-1,-1,-1):
            num2 = num2 + (26**i)*(ord(s[l-i-1])-64)
        print("R"+num+"C"+str(num2))
for _ in range(t):
    s=input()
    typ = func(s)
    convert(typ,s)