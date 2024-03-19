#largest among three number


num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3:"))

if(num1>num2>num3):
    print("Number 1 is largest")
elif(num1<num2>num3):
    print("number 2 is largest")
else:
    print("number 3 is largest")

# OR
#
# if(num1>num2 & num1>num3):
#     print("Number 1 is largest")
# elif(num1<num2 & num2>num3):               instead of & we can also use "and"
#     print("number 2 is largest")
# else:
#     print("number 3 is largest")