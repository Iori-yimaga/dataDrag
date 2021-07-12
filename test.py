# ！/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author Sakuya
# @data 2021/6/29
# @file test.py

from matplotlib import pyplot as plt


def set_ch():
    from pylab import mpl
    mpl.rcParams['font.sans-serif'] = 'SimHei'
    mpl.rcParams['axes.unicode_minus'] = False


set_ch()

plt.title(u'显示中文')
plt.show()
