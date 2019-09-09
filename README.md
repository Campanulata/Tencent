# Tencent_企鹅辅导
目前包含如下功能
* 学情反馈（feedback）
* 数据分析（data_analysis）
* 自动发送vx消息（wechat）
## 一、学情反馈
* 概论

对直播时长，回放时长和作业分数三个维度进行反馈
* 目录结构

feedback.py是主要文件，如果需要修改可以下载，依赖的库有numpy,pandas,xlrd,xlwt,openpyxl
* 使用说明

在dist文件夹中下载feedback.exe，双击打开即可使用
1. 目前导出的学生信息表直播，回放时长和作业分数不准确，需要在该表的直播，回放总时长计算，然后粘贴到对应的列。作业分数需要在班课系统中导出自己求和，再用vlookup合并到基本信息表中（国庆过后新班课系统上线可省略此步）
2. 确保学生基本信息表与此文件在同一目录下
3. 按照提示输入信息
4. 完成后打开feedback.xlsx
## 二、数据分析
## 三、自动发送vx消息
