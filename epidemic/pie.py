import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager as fm
import numpy as np
import pandas as pd

matplotlib.rcParams['font.sans-serif'] = ['SimHei'] #支持中文的细黑体

df = pd.read_csv('total.csv', encoding='utf-8',dtype=np.str)
label_list =df['国家'][:29].to_list()# 各国标签
size = df['确诊'][:29].astype(np.float).astype(np.int).to_list()# 各国确诊人数

'''将确诊人数排在29位之后的国家进行合并处理'''
label_list.append('其他国家')
size.append(df['确诊'][29:].astype(np.float).astype(np.int).sum())

patches, texts, autotexts= plt.pie(size, labels=label_list,
labeldistance=1.1, autopct="%1.1f%%", shadow=True, startangle=0,
pctdistance=0.6)

#调整字体大小
proptease = fm.FontProperties()
proptease.set_size('x-small')
# font size include: ‘xx-small’,x-small’,'small’,'medium’,‘large’,‘x-large’,‘xxlarge’ or number, e.g. '12'
plt.setp(texts, fontproperties=proptease)
plt.setp(autotexts, fontproperties=proptease)
plt.show()