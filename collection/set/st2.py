st={10,20,30,40,50,60,70}

# one elemnt add into the set we use add() add function
st.add(80)
print(st)    # 80 will be added to any position in set
# add function will add only one element at a time
# for add multiple element update function is used   ----> update
st.update([90,100,110])
print(st)



# to remove an element from a set we use
# remove
# discard

st.remove(100)
print(st)

st.discard(50)
print(st)


# difference btw remove and discard
# discard  ---> no error if an unpresent element is entered ---> no return type
# remove   --->  error if an element is not present ----> has return type




# set operations
# union
# intersection
# difference


