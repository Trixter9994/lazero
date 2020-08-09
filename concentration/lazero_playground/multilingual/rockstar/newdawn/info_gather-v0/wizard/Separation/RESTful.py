def sitDown(string):
    env=list(set(string))
    return [[pos,string.count(pos)] for pos in env]
#    return envy
# spread throughtout the center?
# detect the distance?
# yes i am afraid so.
def simpleExam(pos,spliterPosList):
    return [(pos-papi) for papi in spliterPosList]
def reCaptcha(string,spliter):
    return list(enumerate(string.split(spliter)))
#    return ak
# my philosophy is fucked.
# what is unique anyway?
# what is math?
def spliterPos(string,spliter):
    return [pos for pos, char in enumerate(string) if char == spliter]

def spliterPosList(string,spliterList):
    return [pos for pos, char in enumerate(string) if char in spliterList]

def examExist(string,exam):
    return exam in string

#def exchangePos(string,locator):
#    return
#writings="\nhell\nyeah\splitThis\n\n"
# detect overlapped things should I?
#escape=sitDown(writings)
#print(escape)
#enemy=spliterPos(writings,"\n")
#print(enemy)
#print(simpleExam(3,enemy))
#print(examExist(writings,"\n"))
#print(reCaptcha(writings))
#print([writings])
# what to do next?
# to detect what is in the spliter, to decide which split which.
# the invisible spliter?
# the pattern spliter?
# chinese style spliter?
# RULE SPLITER
# FEATURE SPLITER
# LANGUAGE SPLITER
def detectRange(singleChar,validRange):
    night=ord(singleChar)
    if night>=validRange[0] and night<=validRange[1]:
        return True
    else:
        return False
#sorrow="A"
#print(sorrow)
#print(detectRange(sorrow,[4,102]))
#invisibleString="errorISimmediate"
#simpleTaser=(lambda x : detectRange(x,[ord("A"),ord("Z")]))
def atomicRule(string,ruleFunc):
    row=""
    wacon=[]
    for func in list(string):
        if ruleFunc(func):
            row+=func
        else:
            if row!="":
                wacon.append(row)
                row=""
            else:
                pass
    return list(filter((lambda x: x!=""),wacon))
#cancer="SellerNeverDie"
def returnPositionRule(string,ruleFunc):
    return [pos for pos, char in enumerate(string) if ruleFunc(char)]
def returnValidSplitChain(length,splitChain):
#    k0=0
    k1=[]
#    print(splitChain)
    if 0 not in splitChain:
        splitChain.insert(0,0)
#    if length not in splitChain:
    splitChain.append(length)
    # zero to length.
    for k in range(len(splitChain)-1):
        k1.append([splitChain[k],splitChain[k+1]])
#        k0=splitChain[k]+1
#    k1.append([splitChain[len(splitChain)-1],length])
    return list(filter((lambda x: x[0]<x[1]),k1))
def useSplit(string,ruleFunc):
    evil=returnValidSplitChain(len(string),returnPositionRule(string,ruleFunc))
    nightmare=[]
#    print(evil)
    for eve in evil:
        nightmare.append(string[eve[0]:eve[1]])
    return nightmare
#def withDepthMemoryRule(string,ruleFunc,chancellerRule):
#    row=""
#    wacon=[]
#    depth=[]
#    for func in list(string):
#        if ruleFunc(func):
#            depth.append(True)
#        else:
#            depth.append(False)
#    depth0=chacellerRule(depth)
    # get wired.
#    for a,b in enumerate(depth0):
        # this is spliting the thing.
#            if row!="":
#                wacon.append(row)
#                row=""
#            else:
#                pass
#    return list(filter((lambda x: x!=""),wacon))
#print(atomicRule(invisibleString,simpleTaser))
#print(useSplit(cancer,simpleTaser))
