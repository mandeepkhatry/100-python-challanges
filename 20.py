
def generator(n):
    for i in range(0,n):
        if(i%7==0):
            yield i

n = int(input())
for i in generator(n):
    print(i)
