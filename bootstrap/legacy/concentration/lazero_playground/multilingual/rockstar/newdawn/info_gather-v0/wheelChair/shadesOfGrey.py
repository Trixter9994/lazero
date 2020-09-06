#shade0="     set: А, а, Б, б, В, в, Г, г, Ґ, ґ, Д, д, Е, е, Є, є, Ж, ж, З, з, И, и, І, і, Ї, ї, Й, й, К, к, Л, л, М, м, Н, н, О, о, П, п, Р, р, С, с, Т, т, У, у, Ф, ф, Х, х, Ц, ц, Ч, ч, Ш, ш, Щ, щ, Ь, ь, Ю, ю, Я, я"
import os
from oralsex import same_fuck
def neuron(shade,rk,rho):
    horror=list(shade)
    crystal=[]
    if len(horror)>rk:
        for r,k in enumerate(horror):
            if r>rk and r%3==rho:
                crystal.append([k,ord(k)])
    else:
        pass
            # use the index only.
    fuckme=sorted(list(map((lambda x:x[1]),crystal)))
    if len(fuckme)>2:
        init="lua venusWalk.lua"
        for fuckall in fuckme:
            init+=" "+str(fuckall)

#    print(fuckme)
        myCmd0 = os.popen(init)
        myCmd=list(filter((lambda x:x!=""),myCmd0.read().split("\n")))
        if myCmd[0]=='false':
            print("--suck my dick--")
        #for knob in myCmd:
            print(same_fuck(myCmd[1]))
        else:
            pass
        myCmd0.close()
        print("--spilter--")
        for mv in myCmd:
            print(list(filter((lambda x:x!=""),mv.split(" "))))
        print("--spliter--")
    else:
        pass
    return crystal

#print(neuron(shade0,9,1))
