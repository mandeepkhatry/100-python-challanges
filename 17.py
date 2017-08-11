
total=0
while(True):
    check=[]
    n = input()
    if n:
        check = n.split(' ')
        if(check[0]=='D'):
            total +=int(check[1])
        elif(check[0]=='W'):
            total -=int(check[1])
    else:
        break

print(total)