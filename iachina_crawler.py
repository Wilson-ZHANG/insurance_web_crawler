# -*- coding: utf-8 -*-
#description: tkk_02爬取对应哈希值文件的基本信息
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

#url = 'http://www.iachina.cn/IC/tkk/02/efba3adf-dc40-4847-8f9b-ead0d4daf392.html'
#pdf_url = 'http://www.iachina.cn/IC/tkk/03/efba3adf-dc40-4847-8f9b-ead0d4daf392_TERMS.PDF'
def tkk_02(url):#供测试用，main函数里没有用到
    newname = "test.json"
    save = open(newname, 'a+', encoding='utf-8')
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    text = r.text
    soup = BeautifulSoup(text, "html.parser")
    title = soup.find_all('table', {'border': '1'})
    for item in title:
        print(item.find('td',{'align':'right'}).get_text()[:-1],item.find('td',{'align':'left'}).get_text())


def tkk_02_plus_mongojson(url_hash,newname,len):
    url =  'http://www.iachina.cn/IC/tkk/02/'+url_hash+'.html'
    pdf_url = 'http://www.iachina.cn/IC/tkk/03/'+url_hash+'_TERMS.PDF'
    #newname = "test.json"
    save = open(newname, 'a+', encoding='utf-8')
    r = requests.get(url,timeout = 500)
    r.encoding = r.apparent_encoding
    text = r.text
    soup = BeautifulSoup(text, "html.parser")
    title = soup.find_all('table', {'border': '1'})
    for item1 in title:
        print('{"'+item1.find('td', {'align': 'right'}).get_text()[:-1]+'":"'+item1.find('td', {'align': 'left'}).get_text().split()[0]+'",',file=save)
        #print('"pdf_url"',':"',pdf_url,'",',file=save)
        #item = item.next_sibling
        #print(item1.find('td',{'align':'right'}).get_text())
        print("文件",newname,"正在爬取产品",item1.find('td', {'align': 'left'}).get_text()[:-1],"共计",len,"个产品")
        while(item1.find_next('td', {'align': 'right'}).get_text()[:-1].split()[0] != "停止销售日期"):
            try:
                item1 = item1.find_next('td',{'align':'right'})
                kk = item1.find_next('td', {'align': 'right'}).get_text()[:-1].split()[0]
                jj = item1.find_next('td', {'align': 'left'}).find_next('td', {'align': 'left'}).get_text().split()[0]

                if(jj =="在售"):
                    print('"' + kk + '":"' + jj + '",', file=save)
                    #print('"' + kk + '":"' + jj + '",')
                    print('"停止销售日期":" ",', file=save)
                    print('"PDF文件"', ':"' + pdf_url + '"}', file=save)
                else:
                    if(kk =="停止销售日期"):
                        print('"'+kk+'":"'+jj+'",',file=save)
                        print('"PDF文件"', ':"' + pdf_url + '"}', file=save)
                    else:
                        print('"' + kk + '":"' + jj + '",', file=save)
                        #print('"' + kk + '":"' + jj + '",')

            except:
                pass

#tkk_02(url)
#tkk_02_plus_mongojson('af833928-4a41-44e6-bff8-c0e87425bcbe')   #停售 通过test
#tkk_02_plus_mongojson('05ee65ce-0dbb-4cd4-a06a-a4a8418eea45') #停用 通过test
#tkk_02_plus_mongojson('41c96123-580c-4ee6-92b9-c2fe121b23de')

def main():

    li_quota_payment = [""]
    for u1 in li_quota_payment:
        tkk_02_plus_mongojson(u1,'medicare_quota_payment.json',li_quota_payment.__len__())
    li_cost_compensation = [""]
    for u2 in li_cost_compensation:
        tkk_02_plus_mongojson(u2,'medicare_cost_compensation.json',li_cost_compensation.__len__())
    li_disease_others = [""]
    for u3 in li_disease_others:
        tkk_02_plus_mongojson(u3,'disease_others.json',li_disease_others.__len__())
    li_disease_serious = [""]
    for u4 in li_disease_serious:
        tkk_02_plus_mongojson(u4,'disease_serious.json',li_disease_serious.__len__())
    li_disease_cancer = ["1d0f6fb1-d4f6-4abd-8e01-acc19d42c2f6", "cdc58596-63dc-4dee-b6c0-f02161b34bbf", "23e56758-67cc-40f1-bc66-3e52aff2c0b2"]
    for u5 in li_disease_cancer:
        tkk_02_plus_mongojson(u5,'disease_cancer_test.json',li_disease_cancer.__len__())
if __name__ == '__main__':
    main()

