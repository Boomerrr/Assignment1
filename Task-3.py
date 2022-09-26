import pandas as pd
import math
import numpy as np

# 数据读取
FlightPath=pd.read_csv("FlightPath.csv")
LIDARPoints=pd.read_csv("LIDARPoints.csv")

# 飞行坐标数据清理 去掉scanid和n
for index in range(FlightPath.shape[0]):
    if index % 2 != 0:
        FlightPath.drop([index],inplace=True)

# 将飞行坐标数据转换为数组类型
array = np.array(FlightPath)

# 构建坐标点组成的图
graph=np.zeros((34,34))

# 计算每个坐标点到其他点的距离 distance=sqrt((x1-x2)**2+(y1-y2)**2)
for index1 in range(34):
    for index2 in range(34):
        graph[index1][index2]=math.sqrt((array[index1][0]-array[index2][0])**2+(array[index1][1]-array[index2][1])**2)
        if graph[index1][index2]==0:
            graph[index1][index2]=10000

"""--------Dijkstra算法实现---------------"""

# 是否已搜索标记 0表示未搜索 1表示已搜索
search = np.zeros(34)
start = 0
search[start] = 1

# 最短距离记录
distance = np.zeros(34)

# 更新记录
index = np.zeros(34)
n = 0
index[n] = start
n = n+1

# 初始化最短距离表
for i in range(34):
    distance[i] = graph[0][i]

# 循环更新最短距离
for i in range(33):
    min = 0
    # 查找最短路径表中最小值
    for j in range(33):
        if search[j] == 0 and distance[j] < distance[min]:
            min = j
    search[min] = 1
    # 查找记录存入index数组
    index[n] = min
    n = n+1
    # 利用最小值更新最短距离表
    for k in range(34):
        if search[k] == 0 and distance[k] > distance[min]+graph[min][k]:
            distance[k] = distance[min]+graph[min][k]

print("依次选出的顶点为 ")
for index1 in range(33):
     print(index[index1])

print("起点0 - 终点33最短距离 : ", distance[33])





