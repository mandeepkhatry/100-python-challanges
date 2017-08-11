def gen():
    diction={}
    for i in range(1,4):
        diction[i] = i**2
    return diction

print(gen())