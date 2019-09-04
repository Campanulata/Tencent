import pandas as pd
import numpy as np
import os

def feedback(time_live,time_playback,grade,name):
    if time_live > 100 and time_playback>100:
        str1 = '孩子今天表现很好，一共听了' + str(time_live) + '分钟的直播课程，而且下课之后又听了回放，继续保持。'
    elif time_live>100 and time_playback==0:
        str1 = '孩子今天表现很好，一共听了' + str(time_live) + '分钟的直播课程，继续保持~'
    elif time_live>0 and time_playback>0:
        str1 = '孩子早上可能来晚了，听课时长只有' + str(time_live) + '分钟，不过目前孩子已经听了回放，下次记得按时上课~~'
    elif time_live>0 and time_playback==0:
        str1 = '孩子早上可能来晚了，听课时长只有' + str(time_live) + '分钟，麻烦家长督促孩子观看回放，不懂的可以问我或者赵老师。~'
    elif time_live==0 and time_playback>0:
        str1 = '孩子没有来上物理课，不过目前已经看了回放，不懂的可以问我或者赵老师。' 
    else:
        str1 = '孩子早上没有来上物理课，麻烦家长提醒一下孩子及时看回放，不懂得可以问我或者赵老师。' 

    if grade>100:
        str2 = '然后孩子的作业还没有提交，记得提醒孩子完成，我会帮他批改'
    elif grade<60:
        str2 = '然后孩子的作业已经改完了，但是没有及格，今天讲的公式是高一的基石,一定要巩固好。'
    else :
        str2 = '然后孩子的作业已经改完了，掌握的很不错，分数是' + str(grade) + '分，继续保持~'
    
    str0 = '家长您好，和您反馈一下' + str(name) + '的学习情况：'
    str3 = ' '

    str_all =str0 + str1 + str2 + str3

    return str_all

file0 = input("1.请确保学生基本信息表与本程序在同一目录下2.输入工作簿的文件名（不用输入.xlsx）然后按Enter进入下一步")
file_name = file0 + '.xlsx'
times = input("请问反馈第几次的学习情况？输入阿拉伯数字后按Enter") 

df = pd.read_excel(str(file_name))
df['反馈'] = df.apply(lambda row:feedback(row['核心课程第' + str(times)+'节直播'],row['核心课程第' + str(times)+'节回放'],row['核心课程第' + str(times)+'节作业'],row['姓名']),axis=1)
print('打开该目录下的文件：output.xlsx；第73列是需要反馈的信息')
# df[‘直播时长’].astype(‘int’)

path = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(path, '打开此工作簿73列.xlsx')
df.to_excel(output_file,index=False)
