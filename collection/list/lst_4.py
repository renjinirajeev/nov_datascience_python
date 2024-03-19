#odd number sum

lst=[50,80,77,98,69,4,6,5,9,33]
sum=0
for i in lst:
    if(i%2!=0):          #i%2==1
        sum+=i
print(sum)
