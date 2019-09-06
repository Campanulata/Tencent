import pandas as pd
import pandas_profiling
import os

data = pd.read_excel('test1.xlsx')
# data.profile_report('Titanic Dataset')
pandas_profiling.ProfileReport(data)
profile = data.profile_report(title="学习情况数据分析")
profile.to_file(output_file="学习情况数据分析.html")