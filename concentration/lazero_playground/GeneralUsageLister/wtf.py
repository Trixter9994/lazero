import re
a=open("wtf.txt","r")
i=0
p0=[]
while i!=1:
    b=a.readline()
#    print(b)
    try:
        p=re.sub(r'\(.+$','',re.search(r"^.+( - )",b).group(0))
        if p!="":
            print (p)
            p0.append(p)
        else:
            i=1
            break
    except:
        break
a.close()
b=open("MainIndexWithIdenticalKeywords.txt","w+")
for p1 in p0:
    b.write(p1+"\n")
b.close()
