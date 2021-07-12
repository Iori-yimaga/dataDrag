# ！/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author Sakuya
# @data 2021/6/29
# @file for_k.py

import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

# 参数初始化
standardizedfile = 'data/standardized.xls'

# 读取数据
data = pd.read_excel(standardizedfile, index_col=u'基站编号')
# 谱系聚类图
Z = linkage(data, method='ward', metric='euclidean')
P = dendrogram(Z, 0)
# plt.show()
# 输出图片
plt.savefig('output/px.png')
