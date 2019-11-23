# Tencent_企鹅辅导
目前包含如下功能
* 学情反馈(feedback.py)
* 数据分析(data_analysis.py)
* 自动发送vx消息(雷蛇/罗技鼠标)
## 一、学情反馈
### 概论
对直播时长，回放时长和作业分数三个维度进行反馈
### 目录结构
feedback.py是主要文件，如果需要修改，可以直接下载，依赖的库有numpy,pandas,xlrd,xlwt,openpyxl
```
pip install numpy
```
### 使用说明

## 二、数据分析
自动生成图表，源数据在data文件夹内，单个xlsx文件以班级为单位，sheet按次数存档
## 三、自动发送vx消息
wechat.py由于工作微信不能登录网页版微信，客服无法解决，弃;如果发现自己的工作微信可以登录网页版vx，就可以使用feedback搭配wechat.py；否则请使用feedback加雷蛇鼠标方案↓
### 雷蛇鼠标
1. 购买雷蛇/罗技鼠标
2. 导入宏文件
3. 为某侧键绑定该宏
4. 设置由该侧键控制宏的开关
5. 切换vx——切换Excel选中A2单元格——光标仅移动vx搜索框——按下侧键
