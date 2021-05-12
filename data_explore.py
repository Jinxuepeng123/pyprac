#-*- coding: utf-8 -*-
#对数据进行基本的探索
#返回缺失值个数以及最大最小值
#程序代码” data_explore.py”旨在考察每
# 个属性的观测值中空值个数、最大值和最小值。请读懂程序的每行代码，
# 学习与领会pandas库中数据框(dataframe)的基本用法。运行这个程序，
# 并查看运行结果，然后小幅修改代码，完成填写下列表格的空白处。
import pandas as pd

datafile= 'air_data.csv' #航空原始数据,第一行为属性标签
resultfile = 'explore.xlsx' #数据探索结果表

data = pd.read_csv(datafile, encoding = 'utf-8') #读取原始数据，指定UTF-8编码（需要用文本编辑器将数据装换为UTF-8编码）
explore = data.describe(percentiles = [0.25], include = 'all').T #包括对数据的基本描述，percentiles参数是指
# 定计算多少的分位数表（如1/4分位数、中位数等）；T是转置，转置后更方便查阅

explore['null'] = len(data)-explore['count'] #describe()函数自动计算非空值数，空值数需自己动手计算

explore = explore[['null', 'max', 'min','mean','std']]

explore.columns = [u'空值记录数', u'最大值', u'最小值',u'均值',u'标准差'] #表头重命名

'''这里只选取部分探索结果。
describe()函数自动计算的字段有count（非空值数）、unique（唯一值数）、top（频数最高者）、
freq（最高频数）、mean（平均值）、std（标准差）、min（最小值）、50%（中位数）、max（最大值）'''

explore.to_excel(resultfile) #导出结果