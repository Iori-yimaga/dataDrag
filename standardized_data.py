# ！/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author Sakuya
# @data 2021/6/29
# @file standardized_data.py

import pandas as pd

# 参数初始化
# 原始数据文件
ori_data = 'data/business_circle.xls'
# 标准化后数据保存路径
standardizedfile = 'data/standardized.xls'
# 读取数据
data = pd.read_excel(ori_data, index_col=u'基站编号')
# 离差标准化
data = (data - data.min()) / (data.max() - data.min())
data = data.reset_index()
# 保存结果
data.to_excel(standardizedfile, index=False)
