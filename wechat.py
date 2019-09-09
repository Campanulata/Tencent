import itchat 
import random
import pandas as pd
itchat.auto_login(hotReload=True)

friends_list = itchat.get_friends(update=True)
df_name = pd.read_excel('feedback.xlsx',usecols='A')    #获取备注
df_fb = pd.read_excel('feedback.xlsx',usecols='B')      #获取反馈
df = pd.read_excel('feedback.xlsx')
list_name = df_name.values.tolist()
# list_name = str(list_name)                            #转str
list_fb = df_fb.values.tolist()
# list_name = df_name['姓名']
# list_fb = df_fb['反馈']
list_name1 = ['AAA','AAAA']

for x,y in zip(list_name,list_fb):
    # str_name = str(list_name[0])
    user_name = itchat.search_friends(name=str(x))
    print(user_name)           #vxid注入name
    uid = user_name[0]['UserName']
    itchat.send(str(y),uid)
    print(uid)


print(list_name)
print(list_name1)
print(type(list_name))
print(type(list_name1))

