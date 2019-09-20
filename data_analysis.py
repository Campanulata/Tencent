import pandas as pd
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Page, Pie, Timeline
import os
import xlsxwriter

# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType

dfz1 = pd.read_excel('./data/z1.xlsx', usecols='F:J')
dfz2 = pd.read_excel('./data/z2.xlsx', usecols='F:J')


def WorkSumList(df):
    df['第1题'].astype("str")
    df = df.replace('未提交', 0)
    df.loc['row_sum'] = df.apply(lambda x: x.sum())
    # row_sum = df.loc['row_sum']
    list1 = df.loc['row_sum'].tolist()
    return list1

bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(["第1题", "第2题", "第3题", "第4题", "第5题"])
    .add_yaxis("第一次作业", WorkSumList(dfz1))
    .add_yaxis("第二次作业", WorkSumList(dfz2))
    .set_global_opts(title_opts=opts.TitleOpts(title="老赵的崽儿们", subtitle="历次作业柱形图"))
)
bar.render()
'''
def timeline_bar() -> Timeline:
    x = Faker.choose()
    tl = Timeline()
    for i in range(2015, 2020):
        bar = (
            Bar()
            .add_xaxis(x)
            .add_yaxis("商家A", Faker.values())
            .add_yaxis("商家B", Faker.values())
            .set_global_opts(title_opts=opts.TitleOpts("某商店{}年营业额".format(i)))
        )
        tl.add(bar, "{}年".format(i))
    return tl
'''