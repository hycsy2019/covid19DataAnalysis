import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['STZhongsong']    # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False           # 解决保存图像是负号'-'显示为方块的问题

newcase=[]
case=[]
death=[]
cured=[]

'得到每个csv中每一天的各个国家各种数值总计'
def readData():
    '''依次读取csv文件'''
    for i in range(1,16):
        fileNameStr = 'result1/epidemic2020-12-'
        if i<10:
            fileNameStr+='0'+str(i)+'.csv'
        else:
            fileNameStr+=str(i)+'.csv'
        df = pd.read_csv(fileNameStr, encoding='utf-8',dtype=np.str)

        newcase.append(df['新增确诊'].astype(np.float).astype(np.int).sum())
        case.append(df['确诊'].astype(np.float).astype(np.int).sum())
        death.append(df['死亡'].astype(np.float).astype(np.int).sum())
        cured.append(df['治愈'].astype(np.float).astype(np.int).sum())

readData()
#绘制每日新增条形图
plt.style.use('seaborn-muted')  # 设置图像风格
fig,ax = plt.subplots()
#plt.subplot(121)
ax.set_title("全球新增确诊病例变化情况")
ax.set_xlabel("日期")
ax.set_ylabel("新增确诊")
x = np.array(['12-'+str(one) for one in range(1,16)])  # 创建一个numpy数组x
y = np.array(newcase) # 创建一个numpy数组y，内容为x中数据的平方值
plt.bar(x, y, color='pink',width=0.5)  # bar的颜色改为黄色
for a, b in zip(x, y):  # 在直方图上显示数字
    plt.text(a, b / 2, '%d' % b, ha='center', va='center', fontsize=8)
plt.legend(["每日新增确诊"],loc='upper center')
plt.show()

#绘制确诊、死亡、治愈折线图
#plt.subplot(131)
plt.plot(x, case, 'bo',color="red", linewidth=2.0, linestyle="-", label='确诊')
plt.plot(x, death, 'bo', color="b", linewidth=2.0, linestyle="--",label='死亡')
plt.plot(x, cured, 'bo', color="g", linewidth=2.0, linestyle=":",label='治愈')
plt.title('全球累计确诊/死亡/治愈人数变化情况')
plt.xlabel('日期')
plt.ylabel('人数')
plt.legend(["确诊","死亡","治愈"],bbox_to_anchor=(1.01, 0), loc=3, prop={'size': 8})

#plt.subplot(132)

# plt.title('全球累计死亡人数变化情况')
# plt.xlabel('日期（12月）')
# plt.ylabel('人数')
# plt.legend(("死亡人数",),loc='lower center')
#
# #plt.subplot(133)
#
# plt.title('全球累计治愈人数变化情况')
# plt.xlabel('日期（12月）')
# plt.ylabel('人数')
# plt.legend(("治愈人数",),loc='lower center')

plt.show()

