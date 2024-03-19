#Binary Search Algorithm

 # lst=[5,1,7,4,9,2,8,10,3]

 # 1. sort the given list in ascending order
# [1,2,3,4,5,7,8,9,10]
# low                upper


# 2. low=0
# upper=len(lst)-1


# 3.calculate mid = (low+upper)//2 = (0+8)//2 = 4     floor div : to avoid decimals

# A.  search element > lst[mid]
       #low =mid + 1

# B.  search element < lst[mid]
       #upper =mid - 1

# C.  search element == lst[mid]
       #print element found

lst=[5,1,7,4,9,2,8,10,3]
num= int(input("enter a number:"))
lst.sort()
low=0
upper=len(lst)-1
flag=0
iteration=0
for i in lst:
    mid=(low+upper)//2
    if(num>lst[mid]):   #6>5
          low=mid+1   #low=4+1=5
    elif(num<lst[mid]):
          upper=mid-1
    else:
          flag=1
if(flag==1):
    print("element found")
elif(flag==0):
    print("element not found")





