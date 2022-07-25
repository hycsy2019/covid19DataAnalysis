import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('total.csv', encoding='utf-8')
result=df[0:10]

'''输出确诊率、治愈率前10，死亡率后10'''
df1 = df.sort_values(by="确诊率（%）",ascending=False,ignore_index=True)
print(df1[0:10][["国家","确诊率（%）"]])

df2 = df.sort_values(by="死亡率（%）",ascending=True,ignore_index=True)
print(df2[0:10][["国家","死亡率（%）"]])

df3 = df.sort_values(by="治愈率（%）",ascending=False,ignore_index=True)
print(df3[0:10][["国家","治愈率（%）"]])

'''绘制确诊数前10国家确诊率、死亡率、治愈率图形'''
fig,ax=plt.subplots()
plt.rcParams['font.sans-serif'] = ['SimHei'] #添加对中文字体的支持

x=np.arange(1,11) #生成横轴数据
fig, ax = plt.subplots()
ax.set_title("各国疫情数据")
ax.set_xlabel("国家")
ax.set_ylabel("比率")
ax.set_xticklabels(result[0:10]['国家'].to_list())

y1=result[0:10]["确诊率（%）"].to_list()
y2=result[0:10]["治愈率（%）"].to_list()
y3=result[0:10]["死亡率（%）"].to_list()
plt.xticks(range(1,11))
plt.bar(x,y1,0.2,alpha=0.5,color='b')
plt.bar(x+0.2,y2,0.2,alpha=0.5,color='r')
plt.bar(x+0.4,y3,0.2,alpha=0.5,color='y')

plt.legend(["确诊率（%）","治愈率（%）","死亡率（%）"],bbox_to_anchor=(1.01, 0), loc=3, prop={'size': 8})
plt.grid(True, linestyle='--', alpha=0.8) #设置网格线
plt.show()


