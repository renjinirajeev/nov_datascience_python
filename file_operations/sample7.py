f=open('sample7','r')
f1=open('write_sample7','w')
# k='apple'
# for i in f:
#     if k not in i:
#         f1.write(i)
for i in f:
    if(i!='apple\n'):           # if i not in 'apple':
        f1.write(i)