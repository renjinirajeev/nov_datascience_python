# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.


no_of_cls=int(input("Enter the number of class held:"))
no_of_cls_attnd=int(input("Enter the number of class attended:"))

percnt=((no_of_cls_attnd/no_of_cls)*100)
print("percentage of the student is:",percnt)

if(percnt>=75):
    print("The student can sit in exam")
else:
    print("The student is not allowed to sit in exam")