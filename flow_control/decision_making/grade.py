sub1=int(input("Enter the mark of subject 1:"))
sub2=int(input("Enter the mark of subject 2:"))
sub3=int(input("Enter the mark of subject 3:"))
sub4=int(input("Enter the mark of subject 4:"))

print("Mark of subject 1:",sub1)
print("Mark of subject 2:",sub2)
print("Mark of subject 3:",sub3)
print("Mark of subject 4:",sub4)
total=sub1+sub2+sub3+sub4
print('Total mark =',total)

if(total>=180):
    print("Grade is: A+")
elif(160<=total<=179):
    print("Grade is: A")
elif(140<=total<=159):
    print("Grade is: B+")
elif(120<=total<=139):
    print("Grade is: B")
elif(100<=total<=119):
    print("Grade is: C")
elif(80<=total<=99):
    print("Grade is: C+")
else:
    print("Grade is: Fail ")



