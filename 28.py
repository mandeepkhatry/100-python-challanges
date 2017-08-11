

def gen():
    d={}
    for i in range(1,21):
        d[i] = i**2
    return d

for (k,v) in gen().items():
    print(v)