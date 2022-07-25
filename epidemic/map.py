from pyecharts import options as opts
from pyecharts.charts import Map
import pandas as pd
import random

df = pd.read_csv('total.csv', encoding='utf-8')
df=df.sort_values(by='人口',ascending=False)[0:100]#选取人口数前100的国家

class Data:
    provinces = df['国家'].to_list()

    @staticmethod
    def values() -> list:
        return df['确诊'].to_list()


def map1() -> Map:
    c = (Map().add("各国确诊数", [list(z) for z in zip(Data.provinces, Data.values())], "world").set_global_opts(
        title_opts=opts.TitleOpts(title="各国确诊数")))
    return c


def map2() -> Map:
    c = (Map().add("各省大学数量", [list(z) for z in zip(Data.provinces, Data.values())], "china").set_global_opts(
        title_opts=opts.TitleOpts(title="Map2（连续型）"),
        visualmap_opts=opts.VisualMapOpts(min_=20, max_=150)).set_series_opts(label_opts=opts.LabelOpts(is_show=True)))
    return c


#map2().render("map2.html")

map1().render("map1.html")
