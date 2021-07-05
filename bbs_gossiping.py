# bbs八卦版
import requests
from bs4 import BeautifulSoup as bs 
import pandas as pd
Cookieurl = "https://www.ptt.cc/ask/over18"
url="https://www.ptt.cc/bbs/Gossiping/index.html"
payload = {
'from' : '/bbs/Gossiping/index.html', 'yes' : 'yes'}
ress = requests.session()
res = ress.post(Cookieurl, data = payload)
soup = bs(ress.get(url).text, "lxml")
page = soup.select(".btn-group.btn-group-paging a.btn.wide")[1]['href'].split('.')[0].split('x')[1]
df0 = []
for i in range(10):
    url = "https://www.ptt.cc/bbs/Gossiping/index{}.html".format(int(page) +1- i) 

    res = ress.get(url)
    soup = bs(res.text, "lxml")
    for title, date in zip(soup.select('.title'), soup.select('.date')):
        if title.text.find(u"刪除")== -1:
            df0.append({'Date' : date.text, 'Title': title.text.
                        strip(), 'Link' :"https://ww.ptt.cc"+title.a['href']})
'''data的資料 （發佈時間 標題網）'''
df = pd.DataFrame(df0)
