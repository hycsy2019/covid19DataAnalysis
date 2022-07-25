import pandas as pd
import numpy as np

df = pd.read_csv('total.csv', encoding='utf-8')
df=df.sort_values(by='人口',ascending=False)[0:100]#选取人口数前100的国家
df[['确诊率（%）','死亡率（%）','治愈率（%）']]=df[['确诊率（%）','死亡率（%）','治愈率（%）']].astype('float')

'''计算总人口、总感染数、总死亡数'''
total_pop=df['人口'].sum()
total_confirm=df['确诊'].sum()
total_death=df['死亡'].sum()
total_cured=df['治愈'].sum()

'''计算各国人口、确诊、死亡全球占比'''
each_pop=round(100*df['人口']/total_pop,8)
each_confirm=round(100*df['确诊']/total_confirm,8)
each_death=round(100*df['死亡']/total_death,8)
each_cured=round(df['治愈']/total_cured,8)

'''计算指标，进行排名'''
index=(each_confirm*(1-df['治愈率（%）']/100)+each_death)/each_pop
result = pd.concat([df['国家'],index,each_pop,each_death,each_confirm],axis=1,ignore_index=True)
result.columns = ['国家','指标','人口占比','死亡占比','确诊占比']
result=result.sort_values(by='指标',ascending=True)

print(result[0:50])
