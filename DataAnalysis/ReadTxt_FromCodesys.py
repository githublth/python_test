# -*- coding:utf-8 -*-
#文本目的：处理从codesys采集的txt文档

import os

import numpy as np
from scipy import io
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

import linecache  #该模块允许从任何文件里得到任何的行

line_3=linecache.getline('data_100.txt',3)  #读取文件的第3行
Variable_Name=line_3.split()[1:]  #去除第一列的时间列
Variable_Name=[x.replace('[','').replace(']','') for x in Variable_Name] #去除变量名中的[和]字符

data=np.genfromtxt('data_100.txt',delimiter=' ',skip_header=3,encoding='UTF-8') #genfromtxt是一个强大的函数

names=locals()  #利用locals()函数动态生成变量名
for i in range(len(Variable_Name)):  #读取txt中的数据并赋值给变量
    names[Variable_Name[i]]=data[:,i+1]
    names[Variable_Name[i]]=names[Variable_Name[i]][~np.isnan(names[Variable_Name[i]])]  #消去nan值


#保存为.mat数据
dict_data={}
for i in np.arange(len(Variable_Name)):
    dict_data[Variable_Name[i]]=eval(Variable_Name[i])

io.savemat('data.mat',dict_data)   #保存数据为.mat,从而和matlab交互数据


#画图
# 'b':蓝色  ‘g’：绿色 ‘r’：红色  ‘c’：青色 ‘m’：洋红 ‘k’：黑色 ‘w’：白色
plt.figure()
for i in np.arange(len(Variable_Name)):
    if i<6:
        plt.subplot(2,3,i+1)
        plt.plot(eval(Variable_Name[i]))

        matplotlib.rcParams['font.family']='SimHei' #支持中文显示
        plt.xlabel("time(ms)")
        plt.ylabel(Variable_Name[i])
        plt.show()


