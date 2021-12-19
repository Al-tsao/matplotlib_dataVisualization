#載入模組
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randint

#數據載入
axix_x = np.linspace(1, 10, 20)
axix_y = randint(1, 50, 20)
axix_y = axix_y.cumsum()
axix_y2 = axix_x * axix_y

#繪圖
fig = plt.figure()
ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes([0.1, 0.6, 0.4, 0.3])
ax1.plot(axix_x, axix_y, 'r')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_title('Y1 Plot')

ax2.plot(axix_y2, axix_y, 'g')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title('Y2 Plot')

#呈現
plt.show()