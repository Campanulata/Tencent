from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Page, Pie, Timeline,Tab,Line
import os
import xlsxwriter
import pandas as pd
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType
from pyecharts.components import Table
def timeline_bar() -> Timeline:
    tl = Timeline()
    for i in range(1, 9):
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

dfz = pd.read_excel('z.xlsx',usecols=[0,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65])
dfz = dfz[dfz.班级==34753]
dfl = pd.read_excel('l.xlsx',usecols=[0,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65])
dfl = dfl[dfl.班级==24702]

def submission_rate(df):
    df = df.replace(1000,0)
    df = df.replace(2000,0)
    df = pd.DataFrame(df.values.T, index=df.columns, columns=df.index)
    df = df.drop(['班级'])
    # 计算未提交人数
    df['未提交'] = df.apply(lambda x : x.value_counts().get(0,0),axis=1)
    df['提交率'] = 1-df.未提交/(df.columns.size-1)
    df['提交率'] = df['提交率'].apply(lambda x: format(x, '.2'))
    return df['提交率']

xaxis = ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']
for i in range(16):
    xaxis[i] = '第' + str(i+1) + '次'

def line_xaxis_type() -> Line:
    c = (
        Line()
        .add_xaxis(xaxis)
        .add_yaxis('1班_赵丽华', submission_rate(dfz))
        .add_yaxis('4班_李烨', submission_rate(dfl))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="作业提交率"),
        )
    )
    return c


tab = Tab()
tab.add(timeline_bar(), "作业平均分对比")
tab.add(line_xaxis_type(),'作业提交率')
tab.render()
