dic={'id':101,'fname':'Renjini','lname':'Rajeev','age':22,'mark':71}

# value update age=22 ----> 23
#
# dic['age']=23           # dic['age']+=20
# dic['mark']=78
# dic['lname']='R S'
# print(dic)




# add new key value pair
dic['attendence']=89
print(dic)


# to add a new key value pair
del dic['id']
print(dic)


#age presnt or not
print('age'in dic)
print('salary' in dic)
print('salary' not in dic)