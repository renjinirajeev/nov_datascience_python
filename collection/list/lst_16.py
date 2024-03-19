
#second largest number

lst=[1,6,8,15,20,3,100,75,40,45]

i=max(lst)
lst.remove(i)
print('second largest element is:',max(lst))
lst.append(i)
print(lst)

