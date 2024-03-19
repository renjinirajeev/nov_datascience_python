lst=[10,15,5,12,8,12,14,4]      #sum=80
# lst1=[70,65,75,68,72,68,66,76]

lst1=[]
j=0
s=sum(lst)                   #  80-i
for i in lst:
    j=s-i
    lst1.append(j)      # lst1.append(s-i)
print(lst1)

