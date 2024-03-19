#dictionary

#1.  how to define

dic={'id':101,'fname':'vinay','lname':'k','age':28,'prof':'bigdata'}
print(dic)

#2.hetrogeneous data supported

dic={'id':101,'fname': 'renjini','mark':10.55,'value':True}
print(dic)

#3.insertion order is preserved

#4. duplicate support or not
dic={'id':101,'id':102,'fname': 'renjini','mark':10.55,'value':True}  #doesn't support duplicate
# key(second value will generate)
dic={'id':101,'no':101,'fname': 'renjini','mark':10.55,'value':True}   #support duplicate values
print(dic)


#5. Dictionary is mutable