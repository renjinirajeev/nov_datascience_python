# constants count
string='luminartechnolab'
vowels='aeiou'
lst=[]
for i in string:
    if i not in vowels:
        lst.append(i)
print(len(lst))