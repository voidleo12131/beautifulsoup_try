from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time
import pandas as pd
n=1
browser = webdriver.Chrome(executable_path='./chromedriver')
browser.get("https://shopping.pchome.com.tw/")  # 前往PChome網站
 
browser.implicitly_wait(60)  # 隱含等待20秒
# time.sleep(3) 
search_input = browser.find_element_by_id("keyword")  # 查詢文字框
search_input.send_keys("藍芽耳機")  # 輸入文字

 
search_button = browser.find_element_by_id("doSearch")  # 找商品按鈕
search_button.click()  # 點擊

last_height = browser.execute_script("return document.body.scrollHeight")

while n==1:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        print("已經到頁面最底部")
        break
    last_height = new_height
    time.sleep(2)
titles = browser.find_elements_by_class_name("prod_name")  # 取得商品標題
ttile=[]
for x in titles:
    ttile.append(x.text)