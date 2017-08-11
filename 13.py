

n = input()

digits = n.split(" ")

countD = 0
countL=0
for i in n:
    if i.isalpha():
        countL+=1

for i in digits:
    countD+=1

print("LETTERS %d"%countL)
print("DIGITS %d"%countD)
