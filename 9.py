

list = []

while True:
    s = input()
    if s:
        list.append(s.upper())
    else:
        break

for i in list:
    print(i)