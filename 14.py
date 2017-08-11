

n = input()

list = n.split(" ")

countU=0
countL=0



for i in list:
    for j in i:
        if(j.isalpha()):
            if j.isupper():
                countU+=1
            else:
                countL+=1


print("UPPER CASE %d"%countU)
print("LOWER CASE %d"%countL)




