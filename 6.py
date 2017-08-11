
import math
C=50
H=30

d = input()

list = d.split(',')

count =0
for i in list:
    count+=1

l = []
for i in range(count):
    D = int(list[i])
    Q = int(math.sqrt((2*C*D)/H))
    l.append(str(Q))



str = ","

result = str.join(l)

print(result)