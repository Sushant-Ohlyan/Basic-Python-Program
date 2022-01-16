import cmath
a=1
b=5
c=6
d=(b*b)-(4*a*c)
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)
print("The the solution are {0}{1}".format(sol1,sol2))