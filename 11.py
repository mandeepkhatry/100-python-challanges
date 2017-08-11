

import math

def convertToDecimal(x):
    sum =0
    count= 0
    list= []
    for i in x:
        list.append(i)
        count+=1
    list = list[::-1]
    for i in range(0,count):
        sum+=int(list[i])*pow(2,i)
    return sum

n = input()
list = n.split(',')

final = []

for i in list:
    if(convertToDecimal(i)%5==0):
        final.append(i)


print(",".join(final))