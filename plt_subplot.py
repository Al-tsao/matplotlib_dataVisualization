#載入模組
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randint

#數據載入
axix_x = np.linspace(1, 10, 20)
axix_y = randint(1, 50, 20)
axix_y = axix_y.cumsum()
axix_y2 = axix_x * axix_y

#繪圖-連續現在一起，會作圖在同一張圖裡面
plt.plot(axix_x, axix_y)
plt.plot(axix_x, axix_y2)

#繪圖-小圖
plt.subplot(1, 2, 1)
plt.plot(axix_x, axix_y)
plt.subplot(1, 2, 2)
plt.plot(axix_x, axix_y2)

#呈現
plt.show()