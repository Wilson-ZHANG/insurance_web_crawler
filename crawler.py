# -*- coding: utf-8 -*-
#description: url_get爬取当前网页下超链接，easy_crawler_king用于抽取需要信息
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
def url_get():
    html = urlopen('http://bxjg.circ.gov.cn/tabid/5253/ctl/ViewOrgList/mid/16658/OrgTypeID/1/Default.aspx')
    bsObj = BeautifulSoup(html, 'html.parser')
    t1 = bsObj.find_all('a')
    url_li = []
    for t2 in t1:
        t3 = t2.get('href')
        try:
            if(t3[0:11] == '/tabid/5253'):
            #print(t3[:11])
                url_li.append('http://bxjg.circ.gov.cn'+t3)
        except:
            pass
    #print(url_li.__len__())
    j = 0
    while(j < url_li.__len__()):
        easy_crawler_king(url_li[j])
        j+=1

def easy_crawler_king(url):
    newname = "first_try.csv"
    save = open(newname, 'a+', encoding='utf-8')
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    text = r.text
    soup = BeautifulSoup(text, "html.parser")
    title = soup.find('td', {'style': 'color: #1b4098; font-size: 24px; font-weight: bold'})
    li = []
    # print("Title:       ",title.get_text().split())
    li.append(title.get_text().split())
    a = soup.find_all('table', {'class': 'tableRecordProduct'})
    for i in a:
        li.append(i.get_text().split())
    cnt = 3
    print('公司名', li[1][0], li[1][1], li[1][2], file=save)
    while (cnt < li[1].__len__()-2):
        print(li[0][0], li[1][cnt], li[1][cnt + 1], li[1][cnt + 2], file=save)
        cnt = cnt + 3
        print("cnt=",cnt,"len=",li[1].__len__())

url_get()