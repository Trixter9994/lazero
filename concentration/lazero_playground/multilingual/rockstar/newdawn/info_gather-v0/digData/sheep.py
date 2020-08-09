from lolita import fury
dig=[["lop",True,True],["lop",True,False],["lop",False,True],["lop",False,False]]
wrench=[" lop", "  lop   ","lop","lop    "]
tik=0
for m in dig:
    for k in wrench:
        print("--spliter--",tik)
        print(m)
        print("--split--")
        print(k)
        print("--doc--")
        print(fury(m,k))
        print("--hatred--")
        tik+=1
