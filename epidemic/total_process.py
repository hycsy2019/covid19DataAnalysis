import pandas as pd

#处理12-15号数据
epdf=pd.read_csv('result1/epidemic2020-12-15.csv', encoding='utf-8')
podf=pd.read_csv('population.csv', encoding='utf-8')

#与人口表左连接
result=pd.merge(epdf, podf, how='left', on='国家',copy=False, indicator=False,left_index=False)
temp=pd.merge(podf,epdf, how='left', on='国家',copy=False, indicator=False,left_index=False)
print('======================疫情表空值======================')
print(result[result['人口'].isnull().values==True])
print('======================人口表空值======================')
print(temp[temp['确诊'].isnull().values==True])
result=result.dropna(how = 'any')

#添加”确诊率“、”死亡率“、“治愈率”三列
ratio_di=round(100*result['确诊']/result['人口'],4)
ratio_de=round(100*result['死亡']/result['确诊'],4)
ratio_cu=round(100*result['治愈']/result['确诊'],4)
result = pd.concat([result['国家'],result['确诊'],result['治愈'],result['死亡'],result['人口'],ratio_de,ratio_di,ratio_cu],axis=1,ignore_index=True)
result.columns = ['国家','确诊','治愈','死亡','人口','死亡率（%）','确诊率（%）','治愈率（%）']

#输出到csv文件
result.to_csv('total.csv',encoding='utf-8',index=False)