from selenium import webdriver
import pandas as pd
import time
'''搜尋商品'''
search = str(input('搜尋 : '))
'''打開網頁'''
driver = webdriver.Chrome()
'''預設一萬頁'''
pages = range(1,10000)

urls= []
nname=[]
price = []
a = 1

'''先把網址存起來'''
for pages in pages:
    urls.append('https://www.momoshop.com.tw/search/searchShop.jsp?keyword={}&searchType=1&cateLevel=0&cateCode=&curPage={}&_isFuzzy=0&showType=chessboardType'.format(search,pages))
'''執行'''
for f in range(len(urls)):
    '''刷網頁'''
    driver.get(urls[f])
    '''讓網站跑一下'''
    time.sleep(10)
    '''讀取資料'''
    prod = driver.find_elements_by_class_name("prdName")
    '''資料為空時，跳出迴圈'''
    if prod == []:
        a == 0
        break
    if a == 0:
        break
    '''存取資料'''
    for i in prod:
        nname.append(i.text)

    prodprice = driver.find_elements_by_class_name("price")
    for j in prodprice:
        price.append(j.text)
    '''資料為空時，跳出迴圈'''
    if a == 0:
        break
'''做成表格'''
nname= pd.Series(nname)
nname.to_frame()
price = pd.Series(price)
price.to_frame()
Full = {'商品名稱':nname,
        '商品價格':price
        }
news_df = pd.DataFrame(Full)
'''輸出'''
filename = str(input('存檔名稱(簡短一點): '))
news_df.to_excel('{}.xlsx'.format(filename))    
