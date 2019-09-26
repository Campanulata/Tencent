from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Page, Pie, Timeline,Tab
import os
import xlsxwriter
import pandas as pd
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType
from pyecharts.components import Table

def timeline_bar() -> Timeline:
    tl = Timeline()
    for i in range(1, 4):
        df = pd.read_excel('./data/dfz1.xlsx',sheet_name='Sheet' + str(i))
        dfz1 = df['总平均分'].tolist()
        df = pd.read_excel('./data/dfl4.xlsx',sheet_name='Sheet' + str(i))
        dfl4 = df['总平均分'].tolist()
        bar = (
            Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add_xaxis(["第1题", "第2题", "第3题", "第4题", "第5题"])
            .add_yaxis("1班_赵丽华老师", dfz1)
            .add_yaxis("4班_李烨老师", dfl4)
            #左上角标题
            .set_global_opts(title_opts=opts.TitleOpts("第{}节作业".format(i)))
        )
        #时间轴坐标
        tl.add(bar, "{}节".format(i))
    return tl
tab = Tab()
tab.add(timeline_bar(), "作业平均分对比")
tab.render()
