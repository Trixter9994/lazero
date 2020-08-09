import re
# four version.
#shit="Aaaaaaargh fuck!"
# shall use multiline support.
# shall escape things.
def fury(numb,shit):
#    numb0=numb
    shake=(lambda x: re.escape(x))
    nope0=["^","$",".{1,}"]
    mobile=(lambda nope,shit0: list(re.findall(r'{}'.format(nope),shit0)))
    joke=(lambda y: True if len(y)>0 else False)
    font=nope0[0]
    font0=nope0[1]
    if numb[1]==False:
        font+=nope0[2]
    if numb[2]==False:
        font0=(nope0[2]+font0)
    fake=mobile(font+shake(numb[0])+font0,shit)
    return joke(fake)
#print(mobile)
