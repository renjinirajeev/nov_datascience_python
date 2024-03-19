#find second largest among three number

num1=int(input("Enter Number 1:"))
num2=int(input("Enter Number 2:"))
num3=int(input("Enter Number 3:"))

if(num1>num2>num3):
    print("Number 2 is second largest")
elif(num3>num2>num1):
    print("Number 2 is second largest")
elif(num2>num1>num3):
    print("Number 1 is second largest")
elif(num3>num1>num2):
    print("Number 1 is second largest")
elif(num1>num3>num2):
    print("Number 3 is second largest")
else:
    print("Number 3 is second largest")



# #    NESTED IF SYNTAX

# if (condition):
#     if(condition):
#         #statement
#     else:
#         #statement
# elif(condition):
#   if(condition):
#       statement
#   else:
#       statement






