#載入模組
from matplotlib import colors
from matplotlib.patches import Wedge
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randint

#數據載入
labels = ['Frogs', 'Cats', 'Dogs', 'Lions']
sizes = [15, 30, 45, 80]

#繪圖
fig, ax = plt.subplots(dpi = 100)
recipe = ['375 g Flour', '75 g Suger', '250 g Butter', '300 g Berries']

data = [float(x.split(' ')[0]) for x in recipe]
ingredients = [x.split(' ')[-1] for x in recipe]

def func(pct, vals):
    absolute = int(pct/100*np.sum(vals))
    return '{:.1f}%\n({:d} g)'.format(pct, absolute)

wedges, texts, autotexts =  ax.pie(data, autopct = lambda pct: func(pct, data), textprops = dict(color = 'w'))

ax.legend(wedges,ingredients, title = 'Ingredients', loc = 'center left', bbox_to_anchor = (1, 0, 1, 1))

#呈現
plt.show()