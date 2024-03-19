#1. Row count

f=open("C:/Users/RENJINI/Downloads/txn.txt",'r')
count=0
for i in f:
    data=i.rstrip('/n').split(",")
    if i:
        count+=1
print("no of rows:",count)

#------------------------------------------------------------------------------------------

#2 jan month : oid,cusno,category,product,state   row count

f=open("C:/Users/RENJINI/Downloads/txn.txt",'r')
count=0
for i in f:
    data=i.rstrip('/n').split(",")
    date=data[1]
    if(date<='01-31-2011'):
        print(data[0],data[2],data[4],data[5],data[6])
        count+=1
print(count)

# ----------------------------------------------------------------------------
# 3 july month : oid,cusno,category,product,state   row count

f=open("C:/Users/RENJINI/Downloads/txn.txt",'r')
count=0
for i in f:
    data=i.rstrip('/n').split(",")
    date=data[1]
    if('07-01-2011'<= date<='07-31-2011'):
        print(data[0],data[2],data[4],data[5],data[6])
        count+=1
print(count)
# ----------------------------------------------------------------------------

#4 no of categories in reverse order
f=open("C:/Users/RENJINI/Downloads/txn.txt",'r')
dic={}
for i in f:
    data=i.rstrip('\n').split(',')
    cat=data[4]
    if cat not in dic:
        dic[cat]=1
    else:
        dic[cat]+=1
for k, v in sorted(dic.items(), key=lambda x: x[1], reverse=True):
    print(k,",",v)

# ----------------------------------------------------------------------------


# 5  --->   category details

f=open("C:/Users/RENJINI/Downloads/txn.txt",'r')
dic={}
for i in f:
    data=i.rstrip('\n').split(',')
    cat=data[4]
    if cat not in dic:
        dic[cat]=1
    else:
        dic[cat]+=1
for k, v in sorted(dic.items(), key=lambda x: x[1], reverse=True):
    print(k,",",v)
    print(data[0:9])
    break


# -----------------------------------------------------------------------------------


#6    payment method count

f=open("C:/Users/RENJINI/Downloads/txn.txt",'r')
dic={}
for i in f:
    data=i.rstrip('\n').split(',')
    pay=data[8]
    if pay not in dic:
        dic[pay]=1
    else:
        dic[pay]+=1
for k,v in dic.items():
    print(k,",",v)


# -----------------------------------------------------------------------------------

# 7   jan--july month purchase count
f=open("C:/Users/RENJINI/Downloads/txn.txt",'r')
count=0
for i in f:
    data=i.rstrip("/n").split(",")
    date=data[1]
    if("01-01-2011"<=date<='07-31-2011'):
        count+=1
print(count)

#-----------------------------------------------------------------------------------


#8  each category total amount


f=open("C:/Users/RENJINI/Downloads/txn.txt",'r')
dic={}
for i in f:
    data=i.rstrip("/n").split(",")
    cat=data[4]
    amt=float(data[3])
    if cat not in dic:
        dic[cat]=amt
    else:
        dic[cat]+=amt
for k,v in dic.items():
    print(k,",",v)


#---------------------------------------------------------------------------------------------------

# 9 each category maximum amount

f=open("C:/Users/RENJINI/Downloads/txn.txt",'r')
dic={}
for i in f:
    data=i.rstrip("/n").split(",")
    cat=data[4]
    amt=data[3]
    if cat not in dic:
        dic[cat]=amt
    else:
        old=dic[cat]
        if(old<amt):
            dic[cat]=amt
        else:
            dic[cat]=old
for k,v in dic.items():
    print(k,",",v)

#---------------------------------------------------------------------------------------------

#10 average of amount in each category

f=open("C:/Users/RENJINI/Downloads/txn.txt",'r')
dic_sum={}
dic_count={}
for i in f:
    data=i.rstrip("/n").split(',')
    cat=data[4]
    amt=float(data[3])
    if cat not in dic_sum:
        dic_sum[cat]=amt
        dic_count[cat]=1
    else:
        dic_sum[cat]+=amt
        dic_count[cat]+=1
for k,v in dic_sum.items():
    count=dic_count[cat]
    average=v/count
    print(k,",",average)


#---------------------------------------------------------------------------------------

#11 total amount by cash and credit card

sum=0
for i in f:
    data=i.rstrip('/n').split(",")
    amount=float(data[3])
    sum+=amount
print(sum)

# --------------------------------------------------------------------------------

# 12 Indoor games total amount
sum = 0
for i in f:
    data = i.rstrip('\n').split(',')
    cat=data[4]
    amt=float(data[3])
    if(cat=="Indoor Games"):
        sum+=amt
print(sum)


# ---------------------------------------------------------------------------------------------------------


# 13 each state count

dic={}
for i in f:
    data=i.rstrip("/n").split(',')
    state=data[6]
    if state not in dic:
        dic[state]=1
    else:
        dic[state]+=1
for k,v in dic.items():
    print(k,",",v)
