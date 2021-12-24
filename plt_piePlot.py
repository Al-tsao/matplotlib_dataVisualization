#載入模組
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randint

#數據載入
labels = ['Frogs', 'Cats', 'Dogs', 'Lions']
sizes = [15, 30, 45, 80]

#繪圖
fig, ax = plt.subplots(figsize = (4, 4), dpi = 100)
#plt.subplots() is a function that returns a tuple containing a figure and axes object(s). Thus when using fig, ax = plt.subplots() you unpack this tuple into the variables fig and ax.
#https://stackoverflow.com/questions/34162443/why-do-many-examples-use-fig-ax-plt-subplots-in-matplotlib-pyplot-python
explode = (0.1, 0, 0, 0) #要讓哪個部分突出
patches, texts, autotexts = ax.pie(sizes, labels = labels, autopct = '%1.1f%%', shadow = False, startangle = 90, explode = explode) #startangle: 看第一筆資料起始點，90就是時鐘12點，然後往逆時鐘方向排序
plt.setp(autotexts, size = 12, color = 'black') #設定百分比文字大寫及顏色
autotexts[0].set_color('white')

#呈現
plt.show()