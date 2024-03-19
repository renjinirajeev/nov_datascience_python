f=open('sample4','r')
lst=[]
for i in f:
    lst.append(int(i.rstrip('\n')))
print(lst)
print(sum(lst))


#rstrip() - remove a character from right side      lstrip() - remove a character from left side


# data ='hello\n'
# data1=data.rstrip('\n')
# print(data)