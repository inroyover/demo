a=1
for a in  range(101):
    if a%7!=0 and a//10!=7 and a%10!=7:
        print(a)
        a+=1
    else:
        continue
        a+=1
