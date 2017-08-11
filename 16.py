

n=input()

initial = n.split(',')
final=[]
for i in initial:
    if(int(i)%2==1):
        final.append(int(i))

final = [str(x*x) for x in final]

print(",".join(final))

