
p= input()
check =True
passwords = p.split(',')
valid=[]

lC=['$','#','@']
print(passwords)
for password in passwords:
    cU = 0
    cL = 0
    cN = 0
    cC = 0
    if(len(password)>=6)and(len(password)<=12):
        for i in password:
            if i.isalpha():
                if i.upper():
                    cU+=1
                if i.lower():
                    cL+=1
            elif i.isnumeric():
                cN+=1
            elif i in lC:
                cC+=1
        if(cU>=1 and cL>=1 and cN>=1 and cC>=1):
            valid.append(password)

print(",".join(valid))