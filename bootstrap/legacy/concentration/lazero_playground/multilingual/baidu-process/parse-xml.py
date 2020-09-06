# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import re
html0=open("quest-from-baidu.log","r")
html=html0.read()
soup = BeautifulSoup(html, 'lxml')
# result = soup('a',target_="_blank")
#tags = soup.findAll("div",class_="result c-container")

tags = soup.findAll("div",id=re.compile(r"[0-9]+"),class_=re.compile(r'.+(c-contain).+'))
# do not underscore words unless they're reserved.
# class is a reserved word in python.

for tag in tags:
    print(tag)
#from xml.dom.minidom import parse
# import xml.dom.minidom
 
# 使用minidom解析器打开 XML 文档
#DOMTree = parse("quest-from-baidu.log")
#collection = DOMTree.documentElement
#if collection.hasAttribute("shelf"):
#   print "Root element : %s" % collection.getAttribute("shelf")
 
# 在集合中获取所有电影
# movies = collection.getElementsByTagName("")

#if collection.hasAttribute("target"):
#   print ("Root element : " +collection.getAttribute("target"))
html0.close()
