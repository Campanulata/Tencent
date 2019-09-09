import pandas as pd
import numpy as np
import os
import xlsxwriter

def feedback(time_live,time_playback,grade,name):
    if time_live > 100 and time_playback>100:
        str1 = '孩子今天表现很好，一共听了' + str(time_live) + '分钟的直播课程，而且下课之后又听了回放，继续保持。'
    elif time_live>100 and time_playback==0:
        str1 = '孩子今天表现很好，一共听了' + str(time_live) + '分钟的直播课程，继续保持~'
    elif time_live>0 and time_playback>0:
        str1 = '孩子今天早上可能来晚了，听课时长只有' + str(time_live) + '分钟，不过目前孩子已经听了回放，下次记得按时上课~~'
    elif time_live>0 and time_playback==0:
        str1 = '孩子今天早上可能来晚了，听课时长只有' + str(time_live) + '分钟，麻烦家长督促孩子观看回放，不懂的可以问我~'
    elif time_live==0 and time_playback>0:
        str1 = '孩子今天由于时间原因没有参加直播，不过目前已经看了回放，如果有不懂的可以问我~' 
    else:
        str1 = '孩子由于时间原因没有参加今天的直播课，' 

    if grade>100:
        str2 = '然后孩子的作业还没有提交，记得提醒完成，我会帮他批改的，填空题记得把过程也拍下来'
    elif grade<60:
        str2 = '然后孩子的作业已经改完了，但是没有及格，可以看一下解析问题出在哪里或者在群里问我。'
    else :
        str2 = '然后孩子的作业已经改完了，掌握的很不错，分数是' + str(grade) + '分，继续保持~'
    
    str0 = '家长您好，和您反馈一下' + str(name) + '的学习情况：'
    str3 = '^_^'

    str_all =str0 + str1 + str2 + str3

    return str_all

file0 = input("1.请确保学生基本信息表与本程序在同一目录下2.输入工作簿的文件名（不用输入.xlsx）然后按Enter进入下一步")
file_name = file0 + '.xlsx'
times = input("3.请问反馈第几次的学习情况？输入阿拉伯数字后按Enter") 
print('打开该目录下的文件：feedback.xlsx')

# 读取 pd.read_excel(r'D:/source.xlsx', usecols='A:D,H')
df = pd.read_excel(str(file_name))          # 读取数据源表
# df_time = pd.read_excel('df_time.xlsx')     # 读取时间表
# df_grade = pd.read_excel('df_grade.xlsx')   # 读取分数表
# df = pd.merge(df,df_time.loc[:,['学号','核心课程第1节直播','核心课程第1节回放']],how='left',on = '学号') # vlookup 直播，回放时间


df['反馈'] = df.apply(lambda row:feedback(row['核心课程第' + str(times)+'节直播'],row['核心课程第' + str(times)+'节回放'],row['核心课程第' + str(times)+'节作业'],row['姓名']),axis=1)

# df[‘直播时长’].astype(‘int’)
df2 = df[['姓名','反馈']]

# 写入
path = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(path, 'feedback.xlsx')
df2.to_excel(output_file,index=False,engine="xlsxwriter")
# df2.to_excel(output_file,index=False)

