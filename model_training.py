# ！/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author Sakuya
# @data 2021/6/29
# @file model_training.py

import pandas as pd
# 导入sklearn的层次聚类函数
from sklearn.cluster import AgglomerativeClustering

# 参数初始化
# 标准化后的数据文件
standardizedfile = 'data/standardized.xls'
# 聚类数
k = 3
# 读取数据
data = pd.read_excel(standardizedfile, index_col=u'基站编号')

model = AgglomerativeClustering(n_clusters=k, linkage='ward')
# 训练模型
model.fit(data)

# 详细输出原始数据及其类别
# 详细输出每个样本对应的类别
r = pd.concat([data, pd.Series(model.labels_, index=data.index)], axis=1)
# 重命名表头
r.columns = list(data.columns) + [u'聚类类别']
