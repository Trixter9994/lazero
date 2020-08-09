# This is called the metaProgramming and basically any fucking prog lang can do this fuck!
import re
with open("makeDatabase.py","r") as s:
    so=re.findall(r'(""").+(""")',s.read())
    print(so)
    # I need transformation now!
