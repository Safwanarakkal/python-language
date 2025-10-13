n = int(input("enter the total number of colours: "))
colours = []
for i in range(n):
    a=input("enter the colours : ")
    colours.append(a)
print("first and last colours are : " , colours[0] , colours[-1])
