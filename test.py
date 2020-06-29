def func(e):
    return (e[1],e[0])
def uorl(x,y,z):
    if x[0]*(y[1]-z[1]) + y[0]*(z[1]-x[1]) + z[0]*(x[1]-y[1]) > 0:
        return "l"
    elif x[0]*(y[1]-z[1]) + y[0]*(z[1]-x[1]) + z[0]*(x[1]-y[1]) < 0:
        return "u"
    else:
        return "b"
t = int(input())
timepass = input()

for h in range(t):
    dictt = {}
    coor = []
    m=1
    s=int(input())
    for i in range(s):
        x=tuple(map(int,input().split()))
        try:
            tr = dictt[str(x)]
        except:
            dictt[str(x)] = m

        coor.append(x)
        m+=1
    if s==1:
        print("0.00")
        print(1)
        print()
    else:
        coorsor = sorted(coor,key=func)
        lp = coorsor[0]
        rp = coorsor[-1]
        lowerlist = [lp]
        upperlist = [lp]
        for i in range(len(coorsor)):
            if uorl(lp,coorsor[i],rp) == "l" or uorl(lp,coorsor[i],rp) == "b" or i==s-1:
                while (len(lowerlist)>=2) and uorl(lowerlist[-2],lowerlist[-1],coorsor[i]) != "l":
                    lowerlist.pop()
                lowerlist.append(coorsor[i])
            
            if uorl(lp,coorsor[i],rp) == "u" or uorl(lp,coorsor[i],rp) == "b" or i==s-1:
                while (len(upperlist)>=2) and uorl(upperlist[-2],upperlist[-1],coorsor[i]) != "u":
                    upperlist.pop()
                upperlist.append(coorsor[i])

        upperlist.pop()
        upperlist.reverse()
        upperlist.pop()

        fin = lowerlist+upperlist   
        circum = ((fin[0][0]-fin[-1][0])**2 + (fin[0][1]-fin[-1][1])**2)**0.5
        
        for i in range(0,len(fin)-1):
            circum = circum + ((fin[i][0]-fin[i+1][0])**2 + (fin[i][1]-fin[i+1][1])**2)**0.5
        print("%.2f"%circum)
        # print(fin)
        for i in fin[0:-1]:
            print(dictt[str(i)],end=" ")
        print(dictt[str(fin[-1])])
        print()
        ss = input()