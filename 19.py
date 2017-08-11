
from operator import itemgetter

unsorted=[]
while(True):
    n = input()
    if n:
        l = n.split(',')
        unsorted.append((l[0],l[1],l[2]))
    else:
        break

print(sorted(unsorted,key=itemgetter(0,1,2)))

