# #unit
# 100 no charge
# 101-200     1unit=5rs
# above 200   1 unit = 10 rs
# calculate electricity bill


unit=int(input("Enter the units used:"))

c1 = (unit - 100) * 5               #1st 100 units no charges
c2=(unit-200)*10+500                #1st 100 units no charges and
                                    #from 101-200 there is 100 unit
                                    #1 unit--> 5 rs
                                    #100 units --> 500 rs
                                    #unit-200 defines 100 for 1st 100 unit & 100 for 2nd 100 units
if(unit<=100):
    print("No Charge:")
elif(101<=unit<=200):
    print("charge is:",c1)
else:
    print("charge is:",c2)


#           OR
#
# unit=int(input("Enter the units used:"))
# if(unit<=100):
#     amount=0
# elif(unit>100 and unit<=200):
#     amount=(unit-100)*5
# else:
#     (unit - 200) * 10 + 500
# print("amount")
#

