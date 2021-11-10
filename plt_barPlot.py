#載入模組
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randint

#數據載入
b = [10, 23, 43, 5, 66]
a = ['a', 'b', 'c', 'd', 'e']

#繪圖
plt.bar(a, b, width=0.5)

#呈現
plt.show()