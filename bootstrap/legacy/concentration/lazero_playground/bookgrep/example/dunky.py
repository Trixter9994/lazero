import jieba
from getFromPickleR import returnAList
from simpleStorageR import storeFuck
txt = open("all.txt", encoding="utf-8").read()
#加载停用词表
# stopwords = [line.strip() for line in open("CS.txt",encoding="utf-8").readlines()]  
stopword = returnAList()
stopwords=stopword['stopword']+stopword['control']
words  = jieba.cut(txt)
counts = {}  
for word in words:
    #不在停用词表中
    if word not in stopwords:
        #不统计字数为一的词
        if len(word)>1:
            counts[word] = counts.get(word,0) + 1
items,i0 = list(counts.items()),True
items.sort(key=lambda x:x[1], reverse=True)
i0=items[0]
i1=i0[1]
i2=i1**0.33
i3=i2**2
i4,i5,i6,i7,i8=list(map(int,[i3,i2])),0,[],len(items),{"tags":[],"relationships":[]}
for fm in i4:
  for i in range(i5,i7+1):
    if items[i][1]<=fm:
      i5=fm+1
      i6.append(i)
      break
i8["tags"]=items[:i6[0]]
i8["relationships"]=items[i6[0]:i6[1]]
storeFuck(i8)
print(i8)
# for i in range(len(items)):
#     if i0:
#         word, count = items[i]
#         if count<20:
#             i0=False
#         print ("{:<10}{:>7}".format(word, count))
#     else:
#         break
      #pynb?