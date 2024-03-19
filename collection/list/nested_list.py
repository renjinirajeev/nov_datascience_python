#nested list
#list inside a list

lst=[[101,'vinay','vijay',27,'bigdata',10000],
     [102,'ram','k',32,'datascience',20000],
     [103, 'amal','s',23,'python',15000],
     [104,'reshma','g',26,'testing',18000],
     [105,'vivek','m',30,'bigdata',35000]]
# print(lst)   output in a single line
# for i in lst:
    # print(i)  #  output each list in each line
# #age greater than 30
#     if(i[3] > 30):
#        print(i)



#age less than 30  fname,lname,age,prof
# for i in lst:
#     if(i[3]<30):
#         print(i[1:5])  # print(i[1],i[2],i[3],i[4])


# age = 30 fname lname, age
# for i in lst:
#     if(i[3]==30):
#         print(i[1:4])


# bigdata prof fname,lname,age,prof
# for i in lst:
#     if(i[4]=='bigdata'):
#         print(i[1:5])


# python prof fname, age,salary
# for i in lst:
#     if(i[4]=='python'):
#         print(i[1::2])   or   print(i[1:6:2])   or   print(i[1],i[2],i[5])


# bigdata prof and age above 27 fname, age,salary
# for i in lst:
#     if(i[4]=='bigdata' and i[3]>27):
#         print(i[1::2])


# total salary
# for i in lst:
#     print(s)

# sum=0
# for i in lst:
#     sum+=i[5]
# print(sum)


#nested list ---> age mxm one employee fname, lname , age


# oldest=0
# flag=0
# for i in lst:
#      if(i[3]>oldest):
#          oldest = i[3]
#          flag=i
# print(i[1:4])




oldest=0
flag=0
for i in lst:
    if(i[3]>oldest):
        oldest=i[3]
        flag=i
print(flag[1:4])
        



