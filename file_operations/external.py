# age above 22 fname , lname , age


# f=open('C:/Users/RENJINI/OneDrive/Documents/sample4.txt','r')
# for i in f:
#     data=i.strip('\n').split(',')
#     age=data[3]
#     if(age>'22'):
#         print(data[1:4])



# age = 24 fname,lname,age,phn
# f=open('C:/Users/RENJINI/OneDrive/Documents/sample4.txt','r')
# for i in f:
#     data=i.strip('\n').split(',')
#     age=data[3]
#     if(age=='24'):
#         print(data[1:5])


# chennai work location fname , age , location
# f=open('C:/Users/RENJINI/OneDrive/Documents/sample4.txt','r')
# for i in f:
#     data=i.rstrip('\n').split(',')
#     loc=data[5]
#     if(loc=='Chennai'):
#         print(data[1::2])


# age above 23 and loc chennai fname,lname,age,pho,loc
# f=open('C:/Users/RENJINI/OneDrive/Documents/sample4.txt','r')
# for i in f:
#     data=i.rstrip('\n').split(',')
#     age=data[3]
#     loc=data[5]
#     if(age=='23' and loc =='Chennai'):
#         print(data[1:6])



# each location count
f=open('C:/Users/RENJINI/OneDrive/Documents/sample4.txt','r')
dict={}
for i in f:
    data=i.rstrip('\n').split(',')
    loc=data[5]
    if loc not in dict:
        dict[loc]=1
    else:
        dict[loc]+=1
for k,v in dict.items():
    print(k,',',v)
