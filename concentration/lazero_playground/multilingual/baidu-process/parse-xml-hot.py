# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup

html0=open("quest-from-baidu.log","r")
html=html0.read()
soup = BeautifulSoup(html, 'lxml')
# result = soup('a',target_="_blank")
#tags = soup.findAll("div",class_="result c-container")

tags = soup.find("div",class_="FYB_RD")
# do not underscore words unless they're reserved.
# class is a reserved word in python.

#for tag in tags:
print(tags)
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
