

def gen():
    l=[]
    for i in range(1,21):
        l.append(i**2)

    return l

li = gen()
print(li[:5])
print(li[-5:])
print(li[5::])