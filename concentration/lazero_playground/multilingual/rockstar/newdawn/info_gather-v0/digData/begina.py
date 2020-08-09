mild=["56\n5738-\ndg","\n56\n5738-\ndg","56\n5738-\ndg\n","56\n5738-\n","\n5738-\ndg"]
def souviet(union):
    # at head at tail
    mark=list(map((lambda x: [x, False,False]),list(filter((lambda x:x!=""),union.split("\n")))))
    print(mark)
    merge=[x for x,y in enumerate(union) if y=="\n"]
    print(merge)
    quack=len(union)
    # f f t t f t t f
#    gross=[]
#    grass=""
    if merge!=[]:
        if merge[0]==0 and mark[0][1]==False:
            mark[0][1]= True
        if merge[-1]==(quack-1) and mark[-1][2]==False:
            mark[-1][2]=True
        if len(merge)>1:
            if mark[0][2]==False:
                mark[0][2]= True
            if mark[-1][1]==False:
                mark[-1][1]=True
            for mk in range(len(mark)-2):
                print(mk+1)
                mark[mk+1][1], mark[mk+1][2]=True,True
    else:
        pass
    return mark
for jerk in mild:
    print("-----spliter-----")
    print(jerk)
    print(souviet(jerk))
