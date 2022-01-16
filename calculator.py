import math
x=int(input("enter no "))
y=int(input("enter no "))
o=input("enter operater[+,-,*,/,sqrt]::::")
if o=="+":
    result=x+y
elif o=="-":
    result=x-y
elif o=="*":
    result=x*y
elif o=="/":
    result=x/y
elif o=="sqrt":
    result=math.sqrt(x)
else:
    print("invalid operator")
print(x,o,y,"=",result)