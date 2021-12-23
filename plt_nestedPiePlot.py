#載入模組
import matplotlib.pyplot as plt
import numpy as np
from numpy.core.numeric import outer
from numpy.random import randint

#數據載入
vals = np.array([[60, 32], [35, 20], [26, 36]])
vals_sum = vals.sum(axis = 1)
vals_flat = vals.flatten()
print(vals_sum)

#繪圖
fig, ax = plt.subplots(dpi = 100)
size = 0.3
cmap = plt.get_cmap('tab20c')
outer_color = cmap(np.arange(3)*4)
inner_color = cmap(np.arange(6)*3)

ax.pie(vals_sum, radius = 1, colors = outer_color, wedgeprops = dict(width = size, edgecolor = 'w'))
print(outer_color)
ax.pie(vals_flat, radius = 1 - size, colors = inner_color, wedgeprops = dict(width = size, edgecolor = 'w'))
print(outer_color)

#呈現
plt.show()
