st1={1,2,3,4,5,6,7,8,9,10}
st2={6,7,8,9,10,11,12,13,14,15}
# union
st3=st1.union(st2)
print(st3)


# intersection common elements
st3=st1.intersection(st2)
print(st3)


# difference : A-B, A has but not in B
st3=st1.difference(st2)
print(st3)
st3=st2.difference(st1)
print(st3)

