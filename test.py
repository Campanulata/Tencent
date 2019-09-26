from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Page, Pie, Timeline
import os
import xlsxwriter
import pandas as pd
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType
  
def WorkSumList(df,n):
    df['第1题'].astype("str")
    df = df.replace('未提交', 0)
    df.loc['row_sum'] = df.apply(lambda x: x.sum())
    list1 = df.loc['row_sum'].tolist()
    return list1

def timeline_bar() -> Timeline:
    tl = Timeline()
    for i in range(1, 3):
        dfz1 = pd.read_excel('./data/z' + str(i) + '.xlsx', usecols='F:J')
        dfl4 = pd.read_excel('./data/l' + str(i) + '.xlsx', usecols='F:J')

        bar = (
            Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add_xaxis(["第1题", "第2题", "第3题", "第4题", "第5题"])
            .add_yaxis("1班_赵", WorkSumList(dfz1,i))
            .add_yaxis("4班_李", WorkSumList(dfl4,i))
            .set_global_opts(title_opts=opts.TitleOpts("第{}次作业".format(i)))
        )
        tl.add(bar, "{}次".format(i))
    return tl

timeline_bar().render()