import itchat 
import random
import pandas as pd
import numpy as np

def vx(name,fb):
    user_name = itchat.search_friends(name)
    print(user_name)
    uid = user_name[0]['UserName']
    itchat.send(fb,uid)

itchat.auto_login(hotReload=True)                       #登录
friends_list = itchat.get_friends(update=True)          #更新好友

df = pd.read_excel('feedback.xlsx')

print(df_name)

list_name = df_name.values.tolist()
list_fb = df_fb.values.tolist()

df.apply(lambda row:vx(row['姓名'],row['反馈']),axis=1)


