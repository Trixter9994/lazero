from bs4 import BeautifulSoup
# try to manipulate a tag object.
# construct with raw parsers?

def locator(a):
    # fuck it.
    a0,l=0,len(a)
    for x in range(l):
        if a[x]==">":
            a0=x+1
            break
    return [a[0:a0],'</'+a[1]+'>']

b=BeautifulSoup("""<p style="position:absolute;margin:0;padding:0;top:661pt;left:98pt"><span style="font-family:ArialNarrow,sans-serif;font-size:9pt;">046C</span><span style="font-family:Evercyrillic,serif;font-size:9.9998pt;"> Ѭ</span><span style="font-family:MyriadPro,serif;font-size:9pt;"> CYRILLIC CAPITAL LETTER IOTIFIED BIG YUS</span></p>""",features='lxml')
# shall we dance?
b1=list(b('p'))[0]
bs=b1.attrs
print(bs)
# merely a string.
# fuck
res=bs['style'].split("left:") # smart shit?
r=res[1].split("pt")
rx=str(int(r[0])+10)
rv={"style":"left:".join([res[0],"pt".join([rx,r[1]])])}
# plus ten fucking pixels? left?
# res={'style': 'position:absolute;margin:0;padding:0;top:0pt;left:0pt'} # can we modify internal content?
b1.attrs=rv
print(b1)
# s=str(b1)
# print(dir(b1))
# print(s) # CONSTRUCT WITH BEAUTIFULSOUP.
# print(locator(s))