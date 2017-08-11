

n= input()

words = n.split(" ")

dictionary ={}

words.sort()

for i in words:
    dictionary[i] = 0

for i in words:
    if(i in words):
        dictionary[i] = (dictionary[i])+1

for i in dictionary:
    print("%s : %d"%(i,dictionary[i]))