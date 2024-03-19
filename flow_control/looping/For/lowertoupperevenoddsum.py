# lower to upper even sum and odd sum

lower=int(input("enter lower limit:"))
upper=int(input("enter upper limit:"))
even_sum=0
odd_sum=0
for i in range(lower,upper+1):
    if(i%2==0):
        even_sum+=i
    else:
        odd_sum+=i
print("sum of even numbers:",even_sum)
print("sum of odd numbers:",odd_sum)