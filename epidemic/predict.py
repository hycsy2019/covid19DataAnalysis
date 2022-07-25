import numpy as np  # 导入数值计算模块
import pandas as pd  # 导入数据处理模块
import matplotlib.pyplot as plt  # 导入绘图模块
from scipy.optimize import curve_fit  # 导入拟合模块

plt.rcParams["font.sans-serif"] = "SimHei"  # 黑体中文
plt.rcParams["axes.unicode_minus"] = False  # 显示负号

confirm=[]

'''依次读取csv文件'''
for i in range(1,16):
        fileNameStr = 'result1/epidemic2020-12-'
        if i<10:
            fileNameStr+='0'+str(i)+'.csv'
        else:
            fileNameStr+=str(i)+'.csv'
        df = pd.read_csv(fileNameStr, encoding='utf-8')

        confirm.append(df['确诊'].astype(np.float).astype(np.int).sum())

t = [1,2,3,4,5,6,7,8,9,10] # 构造横轴
t=np.array(t)
confirm=np.array(confirm)

# 散点图
fig = plt.figure(figsize=(16, 8))  # 建立画布
ax = fig.add_subplot(1, 1, 1)
ax.scatter(t, confirm[0:10], color="k", label="确诊人数")  # 真实数据散点图
ax.scatter([11,12,13,14,15], confirm[10:15], color="r", label="确诊人数")  # 真实数据散点图

ax.set_xlabel("天数")  # 横坐标
ax.set_ylabel("确诊人数")  # 纵坐标
ax.set_title("确诊人数随时间变化情况")  # 标题

# 拟合
def logistic_increase_function(t,K,P0,r):
    # t:time   t0:initial time    P0:initial_value    K:capacity  r:increase_rate
    #r=0.009
    r=0.01
    exp_value=np.exp(r*(t+330))
    return (K*exp_value*P0)/(K+(exp_value-1)*P0)


coef, pcov = curve_fit(logistic_increase_function, t, confirm[0:10])  # 拟合
print(coef)  # logistic函数参数
y_values = logistic_increase_function(t, coef[0], coef[1], coef[2])  # 拟合y值
ax.plot(t, y_values, color="blue", label="拟合曲线")  # 画出拟合曲线

x = np.array([11,12,13,14,15])
y_predict = logistic_increase_function(x, coef[0], coef[1], coef[2])  # 未来预测
ax.scatter(x, y_predict, color="green", label="未来预测")  # 未来预测散点
ax.legend()  # 加标签

print("============predict=============")
print(y_predict)
print("============real=============")
print(confirm[10:15])

plt.show()


# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# import scipy.optimize as so
# import matplotlib
# matplotlib.rcParams['font.sans-serif'] = ['SimHei'] #支持中文的细黑体
#
# case=[]
#
# '得到每个csv中每一天的各个国家各种数值总计'
# def readData():
#     '''依次读取csv文件'''
#     for i in range(1,16):
#         fileNameStr = 'result1/epidemic2020-12-'
#         if i<10:
#             fileNameStr+='0'+str(i)+'.csv'
#         else:
#             fileNameStr+=str(i)+'.csv'
#         df = pd.read_csv(fileNameStr, encoding='utf-8')
#
#         case.append(df['确诊'].astype(np.float).astype(np.int).sum())
#
# readData()
# fig=plt.figure(figsize=(10,4)) #建立画布
# ax=fig.add_subplot(1, 1, 1)
# ax.scatter([range(1,11)],case[0:10],color="k",label="确诊人数") #真实数据散点图
# ax.scatter([range(11,16)],case[10:15],color="r",label="确诊人数") #真实数据散点图
# ax.set_xlabel("天数") #横坐标
# ax.set_ylabel("确诊人数") #纵坐标
# ax.set_title("确诊人数变化") #标题
# #ax.set_xticklabels(['12-'+str(one) for one in range(1,16)], rotation=30, fontsize=10) #自定义横坐标标签
#
# def logistic(t,K,P0,r): #定义logistic函数
#     exp_value=np.exp(r*(t))
#     return (K*exp_value*41)/(K+(exp_value-1)*41)
#
# coef, pcov = so.curve_fit(logistic, range(1,11), case[0:10]) #拟合
# print(coef) #logistic函数参数
# y_values = logistic(range(1,11),coef[0],coef[1],coef[2]) #拟合y值
# plt.plot(range(1,11),y_values,color="blue",label="拟合曲线") #画出拟合曲线
#
# plt.show()