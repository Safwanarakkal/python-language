import math
"""num1 = int(input("enter the number : "))
num2 = int(input("enter the number : "))
gcd = math.gcd(num1,num2)
print("gcd of two numbers is : " , gcd)"""
num1 = int(input("enter the number1 : "))
num2 = int(input("enter the number 2 : "))
if num1 < num2 :
    min = num1 
else:
    min = num2
gcd = 1
for i in  range(1,min+1):
    if num1%i == 0 and num2%i == 0:
        gcd = i
print(f"gcd of two numbers is : {gcd}")
