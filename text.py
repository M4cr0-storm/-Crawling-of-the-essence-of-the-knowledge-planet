#!/usr/bin/python
# -*- coding: UTF-8 -*-
#获得精华的文字
from bs4 import BeautifulSoup
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

f1 = open("jinhua.html", "r")
print "文件名: ", f1.name
html=f1.read()
print len(html)
f1.close()

soup = BeautifulSoup(html, 'html.parser')


answers=[]

f2=open("answers.txt","a+")

for i in (soup.find_all(attrs={'class':re.compile('topic-pp')})):
    answers.append(i.get_text())

answers.reverse()
for j in answers:
    f2.write(j + '\n')
    f2.write('***********************************************************************************************' + '\n')
f2.close()
