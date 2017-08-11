
final = []
for i in range(1000,3001):
    i = str(i)
    count=0
    count1=0
    for j in i:
        count+=1
    for j in i:
        if(int(i)%2==0):
            count1+=1
    if(count==count1):
        final.append(i)




print(",".join(final))

