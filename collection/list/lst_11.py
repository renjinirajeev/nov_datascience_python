# list slicing



lst=[67,9,89,70,58,56,43,55,2,12,34,26,69,34,22,18,71,40,59,38,47,29,88]
print(lst[1:5])   #from index 1 to 4   ---> [start:stop-1]
print(lst[4:9])
print(lst[5:])    # 5 to end of list
print(lst[:9])    # 0 to 8 of the list
print(lst[5:0])   # empty list
print(lst[4:10:2])   # 2 increment of index   --->  [start:stop:step]
print(lst[1:11:3])   # index no : 1,4,7,10
print(lst[5:0:-1])


# positive indexing  :   left to right   [0 to n-1]
# negative indexing  :   right to left   [-1 to -n]
print(lst[-1])
print(lst[-1:-6:-1])
