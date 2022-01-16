p=int(input("principle : "))
t=int(input("time : "))
if t<=5:
    r=7
elif t>=5 and t<=10:
    r=10
else:
    r=20
si=p*r*t/100
print(si)