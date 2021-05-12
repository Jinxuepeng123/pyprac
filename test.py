import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False   #这两行需要手动设置

plt.subplot(3,2,1)
barWidth=0.25
IT=[12,30,1,8,22]
ECE=[28,6,16,5,10]
CSE=[29,3,24,25,17]
plt.title('柱状图')
br1=np.arange(len(IT))
br2=[x+barWidth for x in br1]
br3=[x+barWidth for x in br2]

plt.bar(br1,IT,width=barWidth,color='r',edgecolor='grey',label='IT')
plt.subplot(3,2,2)
x= np.random.random(100)
y= np.random.random(100)
plt.scatter(x, y, s=x*1000, c=y, marker=(1, 1), alpha=0.8, lw=2, facecolors="none")
plt.xlim(0,1)
plt.ylim(0,1)
plt.title('散点图')
plt.subplot(3,2,3)
labels = ' Frogs',' Hogs', ' Dogs', 'Logs'
sizes = [15, 30, 45, 10]
colors = ['yellowgreen','gold','lightskyblue','lightcoral']
explode = (0,0.1,0,0)# only "explode"the 2nd slice(' Hogs')
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%' , shadow=True, startangle=90)
plt.axis('equal')
plt.title('扇形图')
plt.subplot(3,2,4)
plt.plot([1,2,3,4],[1,4,9,16])
plt.title('折线图')
plt.subplot(3,1,3)
a=np.random.normal(loc=-1, scale=1, size=10000)
plt.title('直方图')
plt.hist(a,bins=100)

plt.show()