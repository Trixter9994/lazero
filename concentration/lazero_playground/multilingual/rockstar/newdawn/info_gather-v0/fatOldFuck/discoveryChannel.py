#text=[1,1,1,2,2,2,3,2,3,3,2,2,2,1,1,1]

def skimmer(a,b):
    signal=False
    c=[]
    for diss in range(len(a)):
        if a[diss]==b:
            if signal==False:
                c.append([diss,diss+1])
                signal=True
            else:
                c[-1][1]=diss+1
        else:
            signal=False
    return c

def notorious(exam):
    exam0=list(set(exam))
    exam1=[]
    for k in exam0:
        exam1.append([k,skimmer(exam,k)])
    return exam1

#print(notorious(text))
#print("--spliter--")
#print(exam1)
#for k in range(len(exam)):
#    if k!=len(exam)-1:
#        if exam[k]==exam[k+1]:
