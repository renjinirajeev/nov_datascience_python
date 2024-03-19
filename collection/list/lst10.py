lst=[1,5,3,2,7,6,8,10]

# 1**1
# 5**2
# 3**3
# 2**4
# 7**5
# 6**6
# 8**7

for i in lst:
    i=i**(lst.index(i)+1)
    print(i)


# j=1
# for i in lst:
#     print(i**j)
#     j+=1