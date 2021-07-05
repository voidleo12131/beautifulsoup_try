import json
import requests
from bs4 import BeautifulSoup
import pandas as pd

'''歷史股利政策'''

print('選一支股票代碼')

print("")

num = str(input("股票代碼 : "))

url ="https://marketinfo.api.cnyes.com/mi/api/v1/TWS%3A{}%3ASTOCK/divided".format(num)

headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}

data= requests.get(url,headers=headers)
if data.status_code == 200:
        data=data.text
        
data= json.loads(data)

datas = data["data"]['divides']

a1 = []
a2 = []
a3 = []
a4 = []
a5 = []
a6 = []
a7 = []
a8 = []
a9 = []

for i in range(len(datas)):
    a1.append(datas[i]['formatDate']) #除權息日
    a2.append(datas[i]['formatPreClose']) #除權息前股價
    a3.append(datas[i]['formatCashDividend']) #現金股利 (元/股)
    a4.append(datas[i]['formatDividendYield']) #現金殖利率
    a5.append(datas[i]['formatStockDividend']) #股票股利 (元/百股)
    a6.append(datas[i]['formatFreeDividend']) #無償配股率
    a7.append(datas[i]['formatIssuanceStockDividend']) #現增配股率
    a8.append(datas[i]['formatCallPrice']) #認購價 (元/股)
    a9.append(datas[i]['formatPassDateRange']) #停止過戶日
    

a1 = pd.Series(a1)
a1.to_frame()
a2 = pd.Series(a2)
a2.to_frame()
a3 = pd.Series(a3)
a3.to_frame()
a4 = pd.Series(a4)
a4.to_frame()
a5 = pd.Series(a5)
a5.to_frame()
a6 = pd.Series(a6)
a6.to_frame()
a7 = pd.Series(a7)
a7.to_frame()
a8 = pd.Series(a8)
a8.to_frame()
a9 = pd.Series(a9)
a9.to_frame()

NET= {
    '除權息日': a1,
    '除權息前股價': a2,
    '現金股利 (元/股)': a3,
    '現金殖利率': a4,
    '股票股利 (元/百股)': a5,
    '無償配股率': a6,
    '現增配股率': a7,
    '認購價 (元/股)': a8,
    '停止過戶日': a9
}


news_df = pd.DataFrame(NET)

news_df.to_excel('{}.xlsx'.format(num))
    

  