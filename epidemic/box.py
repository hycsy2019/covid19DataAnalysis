import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
fm.rcParams['font.sans-serif'] = ['SimHei'] #支持中文的细黑体

#打开CSV文件
fileNameStr = 'total.csv'
df = pd.read_csv(fileNameStr,encoding='utf-8')

#添加文本注释
ax = df.boxplot(column=['确诊'],meanline=True,showmeans=True,vert=True) #修改True的设置
ax.text(1.1,df['确诊'].mean(),df['确诊'].mean())
plt.show()