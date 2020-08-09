from newTestN import toyProject
joker=(lambda nope0:nope0[:-1] if nope0[-1]=="\n" else nope0)
greatWall2=(lambda x: "".join([p for p in x if p !=" " and p !='[' and p != ']']))
shit=''
with open('core.log','r') as fuck:
    shit=fuck.read()
p=[]
with open(joker(shit)+'types.txt','r') as f:
    for j in f.readlines():
        if j[0]!='#' and len(j)>1:
            p.append(greatWall2(joker(j)))
'''
for a,b in enumerate(p):
    print(a,[b])'''

for a in p:
    toyProject(0,[a])
