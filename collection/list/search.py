lst=[1,5,10,15,20,25,30,35,24,68,34,78,54,22]
#element read from console if found print found else not found

num=int(input("enter a number:"))
flag=0
iteration=0
for i in lst:
    if(i==num):
        flag+=1
if(flag==1):
    print("element found",i)
else:
    print("element not found")



#linear search algorithm : searching an element in entire list ,
# which will take n iterations
#so its drawback is increase in time complexity

# to overcome this we use binary search algorithm

