#載入模組
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randint

#數據載入
x = np.linspace(1, 10, 20)
y = randint(1, 50, 20)
y = y.cumsum()
y2 = x * y

#繪圖
fig, ax = plt.subplots(1,2, figsize = (12, 4))
ax[0].plot(x, y)
ax[0].plot(x, y2)
ax[0].set_xticks([1, 4, 9]) #ticks: 設定軸標示
ax[1].plot(x, y**2, 'k')
ax[1].set_ylim([2000, 5000]) #lim: 設定軸的最大最小值
ax[1].set_xlim([-5, 5])
ax[1].set_xticks([1, 4, 9]) #ticks: 設定軸標示
ax[1].set_xticklabels([r'$\alpha$', r'$\beta$', r'$\delta$']) #ticklabels: 將設定的座標標示取代成文字

#呈現
plt.show()