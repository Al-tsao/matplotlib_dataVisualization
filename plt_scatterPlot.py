#載入模組
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randint

#數據載入
axix_x = np.linspace(1, 10, 20)
axix_y = randint(1, 50, 20)
axix_y = axix_y.cumsum()

#繪圖
plt.scatter(axix_x, axix_y, linewidths=2)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('This is a demo plot')

#呈現
plt.show()