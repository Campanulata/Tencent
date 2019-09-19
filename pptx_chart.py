import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts

# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType

dfz1 = pd.read_excel('./data/z1.xlsx', usecols='F:J')
dfz1['第1题'].astype("str")
dfz1.replace('未提交', '')
# sumz1 = dfz1.apply(sum)

print(dfz1.dtypes)
bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(["第1题", "第2题", "第3题", "第4题", "第5题"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
)
bar.render()