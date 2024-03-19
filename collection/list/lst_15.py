# lst=[1,3,6,7,5,3,5,7,8,9,6,5,3,2,3,6,7,8,9,15,14,13,11,10]
#
# #   1 incre 7 dec 3 inc 9 dec 2 inc 15 dec
# lst1=[]
# j=lst[0]
# for i in lst:
#     if(j>=i):
#         print(i)
#         lst1.append(j)
# print(lst1)


lst = [1, 3, 6, 7, 5, 3, 5, 7, 8, 9, 6, 5, 3, 2, 3, 6, 7, 8, 9, 15, 14, 13, 11, 10]
lst1 = [lst[i] for i in range(len(lst)) if i == 0 or i == len(lst) - 1 or lst[i] > lst[i - 1] or lst[i] > lst[i + 1] or lst[i] < lst[i - 1] or lst[i] < lst[i + 1]]

print(lst1)