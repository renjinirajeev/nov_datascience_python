# 1 age above 50 fname, lname , age,prof
# f=open('C:/Users/RENJINI/OneDrive/Documents/customer1.txt','r')
# for i in f:
#     data=i.rstrip('\n').split(',')
#     age=data[3]
#     if(age>'50'):
#         print(data[1:5])



# 2 india work fname,lname,age,prof
# f=open('C:/Users/RENJINI/OneDrive/Documents/customer1.txt','r')
# for i in f:
#     data=i.rstrip('\n').split(',')
#     loc=data[-1]
#     if(loc=='india'):
#         print(data[1:4])


# 3 uk work full data
# f=open('C:/Users/RENJINI/OneDrive/Documents/customer1.txt','r')
# for i in f:
#     data=i.rstrip('\n').split(',')
#     loc=data[-1]
#     if(loc=='uk'):
#         print(data[0:6])


# 4 age above 50 and loc india fname ,age,loc
# f=open('C:/Users/RENJINI/OneDrive/Documents/customer1.txt','r')
# for i in f:
#     data=i.rstrip('\n').split(',')
#     age=data[3]
#     loc=data[-1]
#     if(age>'50' and loc=='india' ):
#         print(data[1::2])



# 5 Dancer prof work fname,lname,age
# f=open('C:/Users/RENJINI/OneDrive/Documents/customer1.txt','r')
# for i in f:
#     data=i.rstrip('\n').split(',')
#     prof=data[4]
#     if(prof=='Dancer'):
#         print(data[1:4])



# 6 pilot prof fname,lname,age
# f=open('C:/Users/RENJINI/OneDrive/Documents/customer1.txt','r')
# for i in f:
#     data=i.rstrip('\n').split(',')
#     prof=data[4]
#     if(prof=='Pilot'):
#         print(data[1:4])



# 7 india work and age range 25 to 40 fname,lname,age
# f=open('C:/Users/RENJINI/OneDrive/Documents/customer1.txt','r')
# for i in f:
#     data=i.rstrip('\n').split(',')
#     age=data[3]
#     loc=data[-1]
#     if('25'<=age<='40' and loc=='india'):
#         print(data[1:4])



# 8. each prof count
# f=open('C:/Users/RENJINI/OneDrive/Documents/customer1.txt','r')
# dic={}
# for i in f:
#     data=i.rstrip('\n').split(',')
#     prof=data[4]
#     if prof not in dic:
#         dic[prof]=1
#     else:
#         dic[prof]+=1
# for k,v in dic.items():
#     print(k,",",v)



# 9 each country count
# f=open('C:/Users/RENJINI/OneDrive/Documents/customer1.txt','r')
# dic={}
# for i in f:
#     data=i.rstrip('\n').split(',')
#     loc=data[-1]
#     if loc not in dic:
#         dic[loc]=1
#     else:
#         dic[loc]+=1
# for k,v in dic.items():
#     print(k,',',v)



# 10 each age group count
f=open('C:/Users/RENJINI/OneDrive/Documents/customer1.txt','r')
dic={}
for i in f:
    data=i.rstrip('\n').split(',')
    age=data[3]
    if age not in dic:
        dic[age]=1
    else:
        dic[age]+=1
for k,v in dic.items():
    print(k,",",v)
