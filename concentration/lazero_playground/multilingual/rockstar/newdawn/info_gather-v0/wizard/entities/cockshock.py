from newTestN import toyProject
joker=(lambda nope0:nope0[:-1] if nope0[-1]=="\n" else nope0)
greatWall2=(lambda x: "".join([p for p in x if p !=" "]))
shit=''
with open('core.log','r') as fuck:
    shit=fuck.read()
p=[]
with open(joker(shit)+'entities.txt','r') as f:
    for j in f.readlines():
        if j[0]!='#' and len(j)>1:
            p.append(list(map((lambda x: greatWall2(x)),joker(j).split(':'))))
'''for a,b in enumerate(p):
    print(a,b)'''
for a in p:
    toyProject(0,[a[1],a[0]])
