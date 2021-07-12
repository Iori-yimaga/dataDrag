---
title: 基于基站定位的商圈分析
subtitle: 聚类算法
description: 这是一次数据挖掘的任务
cover: >-
  https://cdn.jsdelivr.net/gh/Iori-yimaga/PicBed/MyBlog/image-20210701101601434.png
tags:
  - 数据挖掘
  - python
  - 聚类算法
categories:
  - 编程学习
  - python
abbrlink: 52f4aab5
date: 2021-06-30 23:13:26
swiper_index:
swiper_desc:
swiper_cover:
updated:
copyright_author:
copyright_url:
license:
license_url:
---

### 0x00 任务背景
随着个人手机终端的普及，手机移动网络也基本实现了城乡空间区域的全覆盖。根据手机信号在真实地理空间上的覆盖情况，将手机用户时间序列的手机定位数据，映射至现实的地理空间位置，即可完整、客观地还原出手机用户的现实活动轨迹，从而挖掘得到人口空间分布与活动联系的特征信息。
		商圈是现代市场中企业市场活动的空间，同时也是商品和服务享用者的区域。商圈划分的目的之一是研究潜在的顾客分布，以制定适宜的商业对策。

### 0x01 数据挖掘目标

1. 对用户的历史定位数据，采用数据挖掘技术，对基站进行分群。
2. 对不同的商圈分群进行特征分析，比较不同商圈类别的价值，选择合适的区域进行运营商的促销活动。

### 0x02 语句探索与预处理

数据挖掘的目标主要是为了找出高价值的商业圈，高价值的商业圈具有人流大，人均停留时间长的特点。但是工作区在工作日也有人流大，人流时间长的特点，经过分析，选取工作日人均停留时间，周末人均停留时间，凌晨人均停留时间，日均人流能量几个特征进行建模和分析。

首先观察一下原始数据，先选取了前十条观测一下：

![image-20210701101506924](https://cdn.jsdelivr.net/gh/Iori-yimaga/PicBed/MyBlog/image-20210701101506924.png)

可以发现各属性的量级差异比较大，处理不太方便，需要标准化处理一下，数据的标准化是将数据按比例缩放，把他们落入一个小的特定的区间，便于不同单位或量级的指标能进行比较和加权。常用的方法有「离差标准化」、「log函数变换」、「atan函数转换」、「z-score标准化」、「归一化方法」等。

这里我们可以采用离差标准化来处理数据：

```python
import pandas as pd

# 参数初始化
# 原始数据文件
ori_data = 'data/business_circle.xls'
# 标准化文件传输出路径
standardizedfile = 'data/standardized.xls'
# 读取数据
data = pd.read_excel(ori_data, index_col=u'基站编号')
# 离差标准化
data = (data - data.min()) / (data.max() - data.min())
data = data.reset_index()
# 保存结果
data.to_excel(standardizedfile, index=False)
```

![image-20210701101535597](https://cdn.jsdelivr.net/gh/Iori-yimaga/PicBed/MyBlog/image-20210701101535597.png)

可以看出数据已经被归化在[0,1]这个区间内，降低了原始数据的差异对结果的影响。

### 0x03 模型构建与评价

这里可以采用层次聚类的方法对数据集进行层次分解，直到满足某种条件。在已经得到距离值之后，元素间可以被联系起来。通过分离和融合可以构建一个结构。传统上，表示的方法是树形数据结构，层次聚类算法，要么是自底向上聚集型的，即从叶子节点开始，最终汇聚到根节点；要么是自顶向下分裂型的，即从根节点开始，递归的向下分裂。最终去查看每一类商圈的特征。

但是首先要知道分成多少类比较合适，即得出k值：

```python
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dandrogram

# 参数初始化
standardizedfile = 'data/standardized.xls'

# 读取数据
data = pd.read_excel(standardizedfile, index_col=u'基站编号')
# 谱系聚类图
Z = linkage(data, method='ward', metric='euclidean')
P = dendrogram(Z, 0)

plt.savefig('output/px.png')
```

然后观察输出的图片：

![image-20210701101601434](https://cdn.jsdelivr.net/gh/Iori-yimaga/PicBed/MyBlog/image-20210701101601434.png)

可以看出分成了三大类，所以为后续构建模型做了准备工作。就可以构建模型了：

```python
# 显示中文标签
plt.rcParams['font.sans-serif'] = 'SimHei'
lpt.rcParams['axes.unicode_minus'] = False

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
```

然后就可以查看output文件夹的图片了：

![image-20210701101700587](https://cdn.jsdelivr.net/gh/Iori-yimaga/PicBed/MyBlog/image-20210701101700587.png)

![image-20210701101716917](https://cdn.jsdelivr.net/gh/Iori-yimaga/PicBed/MyBlog/image-20210701101716917.png)

![image-20210701101732554](https://cdn.jsdelivr.net/gh/Iori-yimaga/PicBed/MyBlog/image-20210701101732554.png)

注：由于中文显示问题，我把标签都改成英文了，从左到右依次是：「工作日人均停留时间」、「凌晨人均停留时间」、「周末人均停留时间」、「日均人流量」，图的标题是商圈类别1、2、3。

从这三张图分析可知:

\-    「商圈类别1」：工作日人均停留时间、凌晨人均停留时间都很低，周末人均停留时间中等，日人均流量很高。比较符合商业区。

\-    「商圈类别2」：工作日人均停留时间中等、凌晨和周末人均停留时间很长，日均人流量很低。比较符合居住区。

\-    「商圈类型3」：工作日人均停留时间很长，凌晨和周末停留时间较少，日均人流量中等。比较符合办公区。

根据原始数据和这三张图的特点来选择建立商区，需要满足“停留时间”波动较小且在原始数据中的值较大。这样才会有比较好的收益。

