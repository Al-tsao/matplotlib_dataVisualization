#匯入模組
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from numpy.random import randn, randint, uniform, sample

#資料匯入
data = [np.random.normal(0, std, 100) for std in range(1, 3)] #python comprehension: https://www.learncodewithmike.com/2020/01/python-comprehension.html

#繪圖
plt.boxplot(data, vert = True)

#呈現
plt.show()