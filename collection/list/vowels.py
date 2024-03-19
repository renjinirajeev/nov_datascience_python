string='luminartechnolab'
#vowels count
vowels='aeiou'
lst=[]
for i in string:
    if i in vowels:
        lst.append(i)
print(len(lst))