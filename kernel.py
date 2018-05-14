#coding:utf-8
import os
from scipy import stats
import pylab as pl
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
np.set_printoptions(threshold=np.inf)


#读取文件
def read_lines(file_path):
    if os.path.exists(file_path):
        array = []
        with open(file_path, 'r') as lines:
            for line in lines:
                array.append(line)
        return array

#将列表以逗号为分割符，取前len(a)-1列数据，返回一个列表
def cal(array):
    c = []
    for item in array:
        a = item.split(',')
        b = []
        for i in range(len(a)-1):
            b.append(float(a[i]))
        c.append(b)
    return c

def one(array):
    c = []
    for item in array:
        b = []
        b.append(1)
        c.append(b)
    return c

def test(file_path):
    array = read_lines(file_path)
    return cal(array)

def lie(file_path):
    arry=read_lines(file_path)
    return one(arry)


filepath = 'iris.txt'

#读取文件
c = test(filepath)
#将列表转换为数组
Y=np.array(c)
Y = np.mat(Y)
#计算均值向量
X=np.mean(Y,axis=0)
#打印均值向量
#print(X)
z=lie(filepath)
Z=np.array(z)
Z = np.mat(Z)
#得到一个均值矩阵，然后用原矩阵减去，得到中心化后的矩阵
A=Y-np.dot(Z,X)
#print(A)

#求核矩阵
D = np.zeros((150,150))
for i in range(0,150):
    for j in range(0,150):
        D[i,j]=np.dot(A[i,:],A[j, :].T)
#求特殊矩阵W
E = np.zeros((150,150))
for i in range(0,150):
    E[i,i]=D[i,i]
#实现一个矩阵的逆
def trans(m):
    for i in range(len(m)):
        for j in range(i):
            m[i][j], m[j][i] = m[j][i], m[i][j]
    return m
E=trans(E)
#将W矩阵开方取逆
for i in range(0,150):
    E[i,i]=sqrt(E[i,i])
#三个矩阵进行内积，得到最后的规范化核矩阵
F=np.dot(E,D)
F=np.dot(F,E)
#print(F)

###########


#第二种方法，直接对数据进行操作，对每一列数据进行规范化
sum=0
for i in range(0,4):
    for j in range(0,150):
        sum=sum+A[j,i]*A[j,i]

    for k in range(0,150):
        A[k,i]=A[k,i]/sqrt(sum)


#对规范化和中心化后的数据求核矩阵
C = np.zeros((150,150))
for i in range(0,150):
    for j in range(0,150):
        C[i,j]=np.dot(A[i,:],A[j, :].T)
print(C)






