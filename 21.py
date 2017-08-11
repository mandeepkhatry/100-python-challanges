
from math import sqrt
totalX=0
totalY=0
while(True):
    n=input()

    if n:
        l = n.split(' ')
        if(l[0]=="UP"):
            totalY+=int(l[1])

        if(l[0]=="DOWN"):
            totalY-=int(l[1])

        if (l[0] == "LEFT"):
            totalX -= int(l[1])

        if (l[0] == "RIGHT"):
            totalX += int(l[1])

    else:
        break

print(int(sqrt(totalX*totalX+totalY*totalY)))