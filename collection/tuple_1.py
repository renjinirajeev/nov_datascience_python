tu=(10,20,30,40,50,60,70,80,90)
# 50  ---->   100
# imutable
lst=list(tu)
lst[4]=100
tu=tuple(lst)
print(tu)


# if we need to modify an element from a tuple we need to convert the tuple into list then modify
# and then convert the list back to tuple
