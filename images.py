#!/usr/bin/python
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import re
import sys
import os,shutil

reload(sys)
sys.setdefaultencoding('utf-8')

f1 = open("jinhua.html", "r")
print "文件名: ", f1.name
html=f1.read()
print len(html)
f1.close()

soup = BeautifulSoup(html, 'html.parser')

images=[]

for i in (soup.find_all(attrs={'class':re.compile('img_style')})):
    images.append("C:\\Users\\admin\\Desktop\\AWD\\"+i.attrs['src'])

for image in images:
    shutil.move(image, "C:\\Users\\admin\\Desktop\\AWD\\pictures")


