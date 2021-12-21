#載入模組
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randint

#數據載入
df = pd.read_csv('daily-temperature.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

groups = df.groupby(pd.Grouper(freq = 'A'))
#https://stackoverflow.com/questions/32168848/how-to-create-a-pandas-datetimeindex-with-year-as-frequency
keys = groups.groups.keys()

years = pd.DataFrame()

for key in keys:
    years[key] = groups.get_group(key)['Temp'].values

#繪圖
plt.matshow(years.T, aspect = 'auto') #aspect: aspect用於指定熱圖的單元格的大小，預設值爲equal,此時單元格用於是一個方塊，當設定爲auto時，會根據畫布的大小動態調整單元格的大小，用法如下

#呈現
plt.show()