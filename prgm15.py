str1 = "abs"
str2 = "ref"
pos = 1
list1 = list(str1)
list2 = list(str2)
list1[pos],list2[pos] = list2[pos],list1[pos]
new_str1 = "".join(list1)
new_str2 = "".join(list2)
result  = new_str1 + " " + new_str2
print(result)
