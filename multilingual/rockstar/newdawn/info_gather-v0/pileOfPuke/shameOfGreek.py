#shade0="     set: А, а, Б, б, В, в, Г, г, Ґ, ґ, Д, д, Е, е, Є, є, Ж, ж, З, з, И, и, І, і, Ї, ї, Й, й, К, к, Л, л, М, м, Н, н, О, о, П, п, Р, р, С, с, Т, т, У, у, Ф, ф, Х, х, Ц, ц, Ч, ч, Ш, ш, Щ, щ, Ь, ь, Ю, ю, Я, я"
import os
from keepMeSatisfied import same_fuck
from discoveryChannel import notorious

badAss=(lambda y:list(map((lambda x:int(x)),y)))

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
    fuckme0=list(map((lambda x:x[1]),crystal))
    fuckme=[fuckme0]
    if len(fuckme[0])>2:
        incline=sorted(fuckme[0])
        decline=True
        for decease in range(len(incline)):
            if incline[decease]==fuckme[0][decease]:
                pass
            else:
                decline=False
                break
        if decline==False:
            fuckme.append(incline)
            print("NOT THE SAME\nNOT THE SAME")
        else:
            print("THE SAME\nTHE SAME")
        print("\n---reality---\n---reality---\n---reality---")
        for bitchEternity in fuckme:
            init="lua geniusWalk.lua"
            for fuckall in bitchEternity:
                init+=" "+str(fuckall)
#        print(init)

#    print(fuckme)
            myCmd0 = os.popen(init)
            myCmd=list(filter((lambda xn:xn!=""),myCmd0.read().split("\n")))
        #myCmd[1]=list(map((lambda x:int(x)),myCmd[1]))
            dickHead=badAss(list(filter((lambda x:x!=""),myCmd[1].split(" "))))
            if myCmd[0]=='false':
                print("--suck my dick--")
        #for knob in myCmd:
                print(same_fuck(myCmd[1]))
                print("--people eater--")
                print(notorious(dickHead))
            else:
                pass
            myCmd0.close()
            print("--spilter--")
            for mv in myCmd:
                print(mv)
            print("--spliter--")
    else:
        pass
    return crystal

#print(neuron(shade0,9,1))
