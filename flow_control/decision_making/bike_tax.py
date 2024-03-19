# Bike Price
#price above 100000 15% tax
# 50000-100000   10%
# below 50000    5%


price=int(input("Enter the price of bike:"))

if(price>100000):
    tax=(price*15)/100
    #print("tax amount is:",tax)
elif(50000<=price<=100000):
    tax=(price*10)/100
    #print("tax amount is:",tax)
else:
    tax=(price*5)/100
    #print('tax amount is:',tax)
print("tax amount is:", tax)

