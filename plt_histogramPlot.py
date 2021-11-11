#載入模組
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randint

#數據載入
axix_x = np.linspace(1, 10, 20)
axix_y = randint(1, 50, 20)

#繪圖
plt.hist(axix_y, rwidth = 0.8, bins = 30)

#呈現
plt.show()