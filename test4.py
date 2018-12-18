# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 09:45:34 2018

@author: chris
"""

import numpy as np
from os import listdir
import time#加载时间库
import matplotlib.pyplot as plt
from sigmoid.timeTransform import timeTransform
from sigmoid.loadData import loadData
from sigmoid.trainData import trainData
import tensorflow as tf

# =============================================================================
# n=4000
# weigh = np.random.rand(n,1)*np.sqrt(1/(n-1+n))*1e-20
# print(weigh)
# =============================================================================

dataArray = loadData.readData('stock/600291.csv')#读取文件
dataArray=loadData.delData(dataArray,'None')#去掉含None的样本
dataArray =loadData.delData(dataArray,'0.0,0.0,0.0')#去掉含'0.0,0.0,0.0'的样本
del dataArray[0] #去掉第一行表头
dataArray = loadData.dataSplit(dataArray,',')#分割样本特征
dataMat = loadData.delFeature(dataArray,[1,2])#去掉无用特征并转为矩阵
dataMat[:,0] = timeTransform.timetostrf(dataMat[:,0])#把第一行时间转换成时间戳


dataMat = dataMat.astype(float)#矩阵内元素转为浮点数
trainMat = loadData.delFeature(dataMat,[0,1,6,7,9,10,11,12])#去掉无用特征
testMat = trainMat[0,:]
trainMat = np.delete(trainMat,0,axis = 0)
#print(trainMat,testMat)
m,n = np.shape(trainMat)
realMat =  np.delete(dataMat[:,7],m,axis = 0)
'''
realArray = np.array(realMat)
trainArray = np.array(trainMat)
testArray = np.array(testMat)
loadData.storeData('stock/label.csv',realArray)
loadData.storeData('stock/trainArray.csv',trainArray)
loadData.storeData('stock/testArray.csv',testArray)
print(trainArray)
'''

print(data)
learning_rate = 0.5
epochs = 10
batch_size = 100
# placeholder
# 输入图片为28 x 28 像素 = 784
x = tf.placeholder(tf.float32, [None, 784])
# 输出为0-9的one-hot编码
y = tf.placeholder(tf.float32, [None, 10])