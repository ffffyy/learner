#coding:utf-8
import os
from scipy import stats
import pylab as pl
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt


#读取文件
def read_lines(file_path):
    if os.path.exists(file_path):
        array = []
        with open(file_path, 'r') as lines:
            for line in lines:
                array.append(line)
        return array

#以逗号为标志拆开列表，存取前len(a)-1列，得到新的嵌套列表
def cal(array):
    c = []
    for item in array:
        a = item.split(',')
        b = []
        for i in range(len(a)-1):
            b.append(float(a[i]))
        c.append(b)
    return c

#构造值为1的列表
def one(array):
    c = []
    for item in array:
        b = []
        b.append(1)
        c.append(b)
    return c

#读取文件，返回列表类型的数据
def test(file_path):
    array = read_lines(file_path)
    return cal(array)

#得到一个与数据样本行数相同的列表
def lie(file_path):
    arry=read_lines(file_path)
    return one(arry)


filepath = 'magic04.txt'
c = test(filepath)
Y=np.array(c)


'''
#利用现有的公式计算样本协方差
Q=np.cov(Y.T)
#打印出协方差矩阵，比较哪对属性具有最大或最小的协方差
for item in Q:
    print(item)
'''


#求均值多元向量
Y = np.mat(Y)
X=np.mean(Y,axis=0)
#print(X)


#将值为1的列表转为数组再转为矩阵
z=lie(filepath)
Z=np.array(z)
Z = np.mat(Z)
#得到中心化矩阵
A=Y-np.dot(Z,X)
'''
#利用中心点之间的外积计算协方差样本矩阵
a=A.T
sum1=np.dot(a,A)*1/19020
#print(sum1)
'''



'''
#利用中心点之间的外积计算样本协方差矩阵
start = A[0, :]
startzhuan = start.T
#sum2的初始值
sum2=np.dot(startzhuan,start)
#一行一行进行点积并累加结果
for i in range(1,19020):
    arri=A[i,:]
    arrizhuan=arri.T
    sum2=sum2+np.dot(arrizhuan,arri)
print(sum2/19020)
'''


'''
#求第一列与第二列数据的相关性
x=A[:,0]
y=A[:,1]
def multiply(a,b):
    #a,b两个列表的数据一一对应相乘之后求和
    sum_ab=0.0
    for i in range(len(a)):
        temp=a[i]*b[i]
        sum_ab+=temp
    return sum_ab

def cal_pearson(x,y):
    n=len(x)
    #求x_list、y_list元素之和
    sum_x=sum(x)
    sum_y=sum(y)
    #求x_list、y_list元素乘积之和
    sum_xy=multiply(x,y)
    #求x_list、y_list的平方和
    sum_x2 = sum([pow(i,2) for i in x])
    sum_y2 = sum([pow(j,2) for j in y])
    molecular=sum_xy-(float(sum_x)*float(sum_y)/n)
    #计算Pearson相关系数，molecular为分子，denominator为分母
    denominator=sqrt((sum_x2-float(sum_x**2)/n)*(sum_y2-float(sum_y**2)/n))
    return molecular/denominator

print("x_list,y_list的相关系数为：" + str(cal_pearson(x, y)))
pl.plot(x, y,'o')# use pylab to plot x and y
pl.show()# show the plot on the screen
'''



'''
#假设第一列的数据复合正态分布，求其概率密度函数
iq=A[:,0]
#均值
mean=iq.mean()
#方差
std=iq.std()
#范围
data=np.arange(-222,222,1)
#调用概率密度函数
yy=stats.norm.pdf(data,mean,std)
#绘图
plt.plot(data,yy)
plt.show()
'''

'''
#求每一列的方差并打印
for i in range(0,10):
    arri=A[:,i]
    print(arri.var())
    '''







