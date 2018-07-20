import requests
from bs4 import BeautifulSoup

url = 'http://bxjg.circ.gov.cn/tabid/5253/ctl/ViewOrg/mid/16658/ItemID/336474/Default.aspx'
newname ="demo.csv"
save =open(newname,'w',encoding='utf-8')
r=requests.get(url)
r.encoding=r.apparent_encoding
text=r.text
soup=BeautifulSoup(text,"html.parser")
title = soup.find('td',{'style':'color: #1b4098; font-size: 24px; font-weight: bold'})
li = []
#print("Title:       ",title.get_text().split())

li.append(title.get_text().split())
a=soup.find_all('table',{'class':'tableRecordProduct'})
for i in a:
    li.append(i.get_text().split())

cnt = 3
print('公司名',li[1][0],li[1][1],li[1][2],file=save)
while(cnt < li[1].__len__()):
    print(li[0][0],li[1][cnt],li[1][cnt+1],li[1][cnt+2],file=save)
    cnt=cnt+3


