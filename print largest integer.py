x=y=z=0
x=float(input("enter first number:"))
y=float(input("enter second number:"))
z=float(input("enter third number:"))
max=x
if y>max:
    max=y
if z>max:
    max=z
print('largest no is',max)