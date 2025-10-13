list1 = ["red","green","yellow","blue","pista"]
list2 = ["red","green","yellow","blue","pista"]
diff  = [ colors for colors in list1 if colors not in list2]

if diff:
    for colors in diff:
        print(colors)
else:
        print("both list contain same colours")
