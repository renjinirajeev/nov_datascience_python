num1=int(input("Enter Number 1:"))
num2=int(input("Enter Number 2:"))
num3=int(input("Enter Number 3:"))

if(num1>num2 and num1>num3):
    if(num2>num3):
        print("number 2 is second largest: ",num2)
    else:
        print("number 3 is second largest: ", num3)
elif(num2>num1 and num2>num3):
    if (num1 > num3):
        print("number 1 is second largest: ", num1)
    else:
        print("number 3 is second largest: ", num3)
elif(num3>num1 and num3>num2):
   if (num1 > num2):
       print("number 1 is second largest: ", num1)
   else:
       print("number 2 is second largest: ", num2)
else:
    print("invalid")

