#current year

#current month

#current date

#birth year

#birth month

#birth date

#print age

#2023
#11
#24

#2022 11 25 =0

curr_yr=int(input("Enter current year:"))
curr_mnt=int(input("Enter current month:"))
curr_date=int(input("Enter current date:"))
bir_yr=int(input("Enter birth year:"))
bir_mnt=int(input("Enter birth month:"))
bir_date=int(input("Enter birth date:"))


age=curr_yr-bir_yr
m=curr_mnt-bir_mnt
day=curr_date-bir_date
if(age>0):
    if(m>0):
        print("Age is:",age)
    elif(m==0)&(day>=0):
        print("Age is:",age)
    elif(m==0)&(day<0):
        print("Age is:",age-1)
    else:
        print("Age is:",age-1)
elif(age==0):
    if (m > 0):
        print("Age is:",age)
    elif (m == 0) & (day >= 0):
        print("Age is:",age)
    elif (m == 0) & (day < 0):
        print("Enter valid age")
    else:
        print("enter valid age")
else:
    print("valid year")



