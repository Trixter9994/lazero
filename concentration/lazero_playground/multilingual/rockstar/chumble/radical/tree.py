import uuid, ast, time
fuckme=1
def shallow():
    global fuckme
    fuckme+=0.13
    fuckme=fuckme**1.01273249
    return fuckme
def realshit():
    fuck=uuid.uuid4().hex
    meow=ast.literal_eval("0x"+fuck.lower())
# this is decimal already.
    cat=str(meow)
#print(cat)
#print("normal cat")
    ranger=(lambda x: range(len(x)))
    fuckall=list(map((lambda x:int(x)+shallow()),list(cat)))
#for m in ranger(cat):
#    fuckall.append("")
    for k in ranger(cat):
#(int i=arr.size()-1;i>=0;--i)
#	{
        vendetta=int(((142857-k)**(time.time()%1+k*0.5)//1)+((271828+2*k)*(time.time()%1-k)//1))
        init=vendetta%(k+1)
        fuckall[init],fuckall[k]=fuckall[k],fuckall[init]
    return meow,fuckall

def boom(hexer):
    # division by zero! you fucking genius!
    hex0,hex1=hexer()
#    print(hex0)
#    print("-----spliter-----")
#    print(hex1)
    reminder=len(hex1)
    for x in range(reminder//2):
        hex0=(hex0/hex1[2*x])*hex1[2*x+1]
    if reminder%2==1:
        hex0=hex0/hex1[-1]
    return hex0

def trust():
    ducky=boom(realshit)
#print("-----spliter-----")
#print(ducky)
    stun=(ducky*0.13)%0.139
    return stun
#print(stun)
taser=trust()
print(taser)
#for k in range(3):
#		srand((unsigned)time(NULL));
    
#		swap(arr[rand()%(i+1)],fuck);

#	}

