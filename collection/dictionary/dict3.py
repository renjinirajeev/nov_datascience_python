line='cat rat bat hello cat rat bat hello cat'

# wordcount   :   no of repetation of a word in a sentence
# cat :3
# rat : 2
# bat : 2
# hello : 2


# word by word data split ----->  split   [list]
# space seperation and comma seperation

data = line.split(' ')
    # word by word seperated in a list

dic={}
for i in data:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)



