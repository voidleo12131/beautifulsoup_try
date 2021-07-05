import requests
import json
import pandas as pd
import numpy as np 
import time

url = "https://covid-19.nchc.org.tw/data/world_timeline.js"
headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
datas = requests.get(url ,verify=False).text
time.sleep(3)

datas=datas.replace("var covid_world_timeline = ","")
dar= json.loads(datas)

#原始資料
rawdata = pd.DataFrame(dar)

#處理原始資料
firstdata =[]
for i in range(len(rawdata)):
    firstdata.append(rawdata["list"][i])
for j in range(len(firstdata)):
    x = firstdata[j]
    y= pd.DataFrame(x).T
    a = y.loc["id"]
    y.columns=pd.Series(a)
    y = y.iloc[0:3]
    firstdata[j]=y

#時間
total_time = rawdata["date"]
total_time = pd.DataFrame(total_time)

#死亡
death = []
for i in range(len(firstdata)):
    death.append(firstdata[i].iloc[1])
Deaths = pd.DataFrame(death)
Deaths = Deaths.reset_index(drop=True)
Deaths.index=pd.Series(total_time["date"])
Deaths.to_excel("Deaths.xlsx")

#確診
confirm = []
for i in range(len(firstdata)):
    confirm.append(firstdata[i].iloc[0])
Confirmed = pd.DataFrame(confirm)
Confirmed = Confirmed.reset_index(drop=True)
Confirmed.index=pd.Series(total_time["date"])
Confirmed.to_excel("Confirmed.xlsx")  

#康復
recover = []
for i in range(len(firstdata)):
    recover.append(firstdata[i].iloc[2])
Recovered = pd.DataFrame(confirm)
Recovered = Recovered.reset_index(drop=True)
Recovered.index=pd.Series(total_time["date"])
Recovered.to_excel("Recovered.xlsx")  
