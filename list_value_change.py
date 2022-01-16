l=[1,2,3,4,5,6,7,8,9,10,11,12]
m=len(l)
for n in range(m):
    if l[n]>10:
        l[n]=10
        print(l)