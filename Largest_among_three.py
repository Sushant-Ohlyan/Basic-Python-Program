num1=10
num2=20
num3=30
if(num1>num2)and(num1>num3):
    largest = num1
elif(num2>num1)and(num2>num3):
    largest = num2
elif(num3>num1)and(num3>num2):
    largest = num3
print("largest number is : ",largest)