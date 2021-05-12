import numpy as np
from sklearn import linear_model
from math import sqrt

from pandas import read_csv

f=open('data-train.csv',encoding='UTF-8')
#names=['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','f13','target']
data=read_csv(f)
train_features=data[:,:-1]

print(data)