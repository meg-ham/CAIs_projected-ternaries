%matplotlib inline
import ternary
print("Version", ternary.__version__)

import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, savefig

import pandas as pd
import numpy as np

# import Excel (.xlsx) file with plottable values [os = Mac version]
import os
f = os.path.expanduser('~/Desktop/Excel Conversion [pyroxene_triplot].xlsx')
df = pd.read_excel(f)

# define visual parameters and plot space
matplotlib.rcParams['figure.dpi'] = 200
matplotlib.rcParams['figure.figsize'] = (11, 9.5)
scale = 100
figure, tax = ternary.figure(scale=scale)

# draw boundary of plot
tax.boundary(linewidth=1)

# set background color of plot [alpha = transparency level]
tax.set_background_color(color="none", alpha=0)

# set axis labels and title
fontsize = 11
tax.set_title("Pyroxene Compositions (wt%) projected\nfrom Enstatite and Quartz\n\n(All Ti as Ti4+)\n", loc='left', fontsize=fontsize, fontweight="bold")
tax.right_corner_label("Tsch", fontsize=fontsize, offset=0.14, fontweight="bold")
tax.top_corner_label("Ca-Tsch", fontsize=fontsize, offset=0.17, fontweight="bold")
tax.left_corner_label("Di", fontsize=fontsize, offset=0.14, fontweight="bold")

# set tick marks
tax.ticks(axis='lbr', linewidth=1, multiple=5)

# remove default Matplotlib axes
tax.clear_matplotlib_ticks()
tax.get_axes().axis('off')

# present data
markers = [] #marker type
fcolors = [] #face color of marker
ecolors = [] #edge color of marker

# run model:
groups=df.groupby('Sample')
names = groups.groups.keys()
for n,i in enumerate(names):
    rows = df.loc[df['Sample']==i]
    x = np.array(rows['Tsch to plot'])
    y = np.array(rows['Ca-Tsch to plot'])
    z = np.array(rows['Di to plot'])
    points=[]
    
    for count,value in enumerate(x):
        points.append((x[count],y[count],z[count]))

    tax.scatter(points, marker=markers[n], s=75, facecolor=fcolors[n], edgecolor=ecolors[n], linewidth=0.3, label=i, zorder=10)

# add legend; this will plot it in the most suitable area of the figure
tax.legend(loc='best')

# save plots
ternary.plt.savefig('pyroxene_triplot', transparent=True)

# show plots
ternary.plt.show()
