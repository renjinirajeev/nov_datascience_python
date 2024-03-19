exp=int(input("Enter the year of experience:"))
salary=int(input("enter your salary:"))
if(exp>=5):
    bonus= salary*5/100
    print("net bonus is:",bonus)      #(salary*0.05)
else:
    print("no bonus")



# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.