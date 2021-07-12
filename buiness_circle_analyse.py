# ！/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author Sakuya
# @data 2021/6/29
# @file buiness_circle_analyse.py

import matplotlib.pyplot as plt
import model_training

# 显示中文标签（但是没用）
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

style = ['ro-', 'go-', 'bo-']
xlabels = ['Average stay time in working days', 'Average stay time in the morning', 'Average length of stay on weekends', 'Average daily passenger flow']
# 聚类图文件名前缀
pic_output = 'output/pic_'

# 逐一作图，作出不同样式
for i in range(model_training.k):
    plt.figure()
    # 提取每一类
    tmp = model_training.r[model_training.r[u'聚类类别'] == i].iloc[:, :4]
    for j in range(len(tmp)):
        plt.plot(range(1, 5), tmp.iloc[j], style[i])

    # 坐标标签
    plt.xticks(range(1, 5), xlabels, rotation=20)
    # 调整计数从1开始
    plt.title('Business district category%s' % (i + 1))
    # 调整底部
    plt.subplots_adjust(bottom=0.15)
    # 输出图片
    plt.savefig(u'%s%s.png' % (pic_output, i + 1))
