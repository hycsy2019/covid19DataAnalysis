import numpy as np
import pandas as pd
import time

#打开CSV文件
for i in range(1,16):
    fileNameStr = 'epidemic2020-12-'
    if i<10:
        fileNameStr+='0'+str(i)+'.csv'
    else:
        fileNameStr+=str(i)+'.csv'
    df = pd.read_csv(fileNameStr, encoding='utf-8',dtype=np.str)

    #2.查看数据集的基本情况
    print("2:head============================================================================")
    print(df.head())
    print("2:describe============================================================================")
    print(df.describe())
    print("3:info============================================================================")
    print(df.info())

    #3.查看是否有缺失值
    print("4============================================================================")
    print(df.isnull().sum().sort_values(ascending=False))

    #将'-'换成'0'
    for i in df.columns:
        df[i]=df[i].str.replace('-','0')

    #将"确诊"变为整型
    df['确诊'] = df['确诊'].astype(np.float).astype(np.int)

    #按照累计确诊倒序排序
    df=df.sort_values(by='确诊',ascending=False)

    #输出到文件
    df.to_csv('result1/'+fileNameStr, encoding="utf-8",index=False)
