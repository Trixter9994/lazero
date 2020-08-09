import jieba
from getFromPickleR import returnAList
txt = open("all.txt", encoding="utf-8").read()  
#加载停用词表  
# stopwords = [line.strip() for line in open("CS.txt",encoding="utf-8").readlines()]  
stopwords=returnAList()['stopword']
words  = jieba.lcut(txt)  
counts = {}  
for word in words:  
    #不在停用词表中  
    if word not in stopwords:  
        #不统计字数为一的词  
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word,0) + 1  
items,i0 = list(counts.items()),True
items.sort(key=lambda x:x[1], reverse=True)
for i in range(len(items)):
    if i0:
        word, count = items[i]
        if count<20:
            i0=False
        print ("{:<10}{:>7}".format(word, count))
    else:
        break
      #pynb?