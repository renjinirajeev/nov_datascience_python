#empty list
# 1 to 100 elements
#even number to a list
#odd number to a list

#list sum
# even list sum
# odd list sum

lst=[]
evenlst=[]
oddlst=[]
for i in range(1,101):
    lst.append(i)
    if(i%2==0):
        evenlst.append(i)
    else:
        oddlst.append(i)
print(lst)
print(evenlst)
print(oddlst)
print(sum(lst))
print(sum(evenlst))
print(sum(oddlst))

