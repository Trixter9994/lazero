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
writings="\nhell\nyeah\splitThis\n\n"
# detect overlapped things should I?
escape=sitDown(writings)
print(escape)
enemy=spliterPos(writings,"\n")
print(enemy)
print(simpleExam(3,enemy))
#print(examExist(writings,"\n"))
#print(reCaptcha(writings))
print([writings])
# what to do next?
