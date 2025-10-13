my_dict  = {"banana":8 , "apple":9 , "orange": 6}
a_dict =  dict(sorted(my_dict.items()))
d_dict =  dict(sorted(my_dict.items() ,reverse=True))
print("sorted in ascending order : " , a_dict)
print("sorted in ascending order : " , d_dict)
