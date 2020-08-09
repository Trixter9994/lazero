import uuid, ast, time
fuck=uuid.uuid4().hex
meow=ast.literal_eval("0x"+fuck.lower())
# this is decimal already.
cat=str(meow)
print(cat)
print("normal cat")
ranger=(lambda x: range(len(x)))
fuckall=list(cat)
#for m in ranger(cat):
#    fuckall.append("")
for k in ranger(cat):
#(int i=arr.size()-1;i>=0;--i)
#	{
    vendetta=int(((142857-k)**(time.time()%1+k*0.5)//1)+((271828+2*k)*(time.time()%1-k)//1))
    init=vendetta%(k+1)
    fuckall[init],fuckall[k]=fuckall[k],fuckall[init]
print(fuckall)
#		srand((unsigned)time(NULL));
    
#		swap(arr[rand()%(i+1)],fuck);

#	}

