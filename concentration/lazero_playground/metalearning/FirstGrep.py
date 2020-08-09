import jieba
a=open("WordsExample/1.log","r",encoding="utf-8")
p=" ".join(jieba.cut(a.read()))

b=open("1.summary","w+")
b.write(p)

a.close()
b.close()
