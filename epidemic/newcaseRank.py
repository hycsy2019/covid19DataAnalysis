import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['STZhongsong']    # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False           # 解决保存图像是负号'-'显示为方块的问题

total={}
everyday={}

'''将所有国家15天的新增病例总数转化为字典'''
def readData():
    global total
    '''依次读取csv文件'''
    for i in range(1,16):
        fileNameStr = 'result1/epidemic2020-12-'
        if i<10:
            fileNameStr+='0'+str(i)+'.csv'
        else:
            fileNameStr+=str(i)+'.csv'
        df = pd.read_csv(fileNameStr, encoding='utf-8',dtype=np.str,usecols=[0,1])
        df['新增确诊']=df['新增确诊'].astype(np.float).astype(np.int)

        for j in range(0, len(df)):
            if not df.iloc[j]['国家'] in everyday.keys():
                everyday[df.iloc[j]['国家']]=[]
            everyday[df.iloc[j]['国家']].append(df.iloc[j]['新增确诊'])

        if i==1:
            total=df.set_index('国家').T.to_dict('int')['新增确诊']
        else:
            for j in range(0, len(df)):
                if df.iloc[j]['国家'] in total.keys():
                    total[df.iloc[j]['国家']] += df.iloc[j]['新增确诊']

readData()

'''取新增病例总数前10的国家'''
top=sorted(total.items(),key=lambda x:x[1],reverse=True)[0:10]

'''绘制折线图'''
fig,ax = plt.subplots()
x = np.array(['12-'+str(one) for one in range(1,16)])
plt.title('每日新增确诊数累计排名前10个国家的每日新增确诊数据的曲线图')
plt.xlabel('日期')
plt.ylabel('新增病例')
country=[]
for each in top:
    plt.plot(x, everyday[each[0]], linewidth=2.0,label=each[0])
    country.append(each[0])
plt.legend(country,bbox_to_anchor=(1.01, 0), loc=3, prop={'size': 8})
plt.show()