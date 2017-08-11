

n = input()

l = [int(x) for x in n.split(',')]

r = l[0]

c= l[1]

matrix = []

for i in range(r):
    temp =[]
    for j in range(c):
        temp.append(i*j)
    matrix.append(temp)

print(matrix)
