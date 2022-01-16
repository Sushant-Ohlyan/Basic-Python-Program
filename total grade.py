a=int(input("enter no"))
b=int(input("enter no"))
c=int(input("enter no"))
d=int(input("enter no"))
e=int(input("enter no"))
total=a+b+c+d+e
per=(total/500)*100
print(per,total)
if per>=90:
        print("that is: a+")
elif 80<= per and  per<90:
        print("that is a-")
elif 60<= per and  per<80:
        print("that is b")
else:
        print("failllll")