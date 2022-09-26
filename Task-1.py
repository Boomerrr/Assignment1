import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

# 数据读取
FlightPath = pd.read_csv("FlightPath.csv")
LIDARPoints = pd.read_csv("LIDARPoints.csv")

# 飞行路径文件 数据清理 去除scanid和n
for index in range(FlightPath.shape[0]):
    if index % 2 != 0:
        print(index)
        FlightPath.drop([index],inplace=True)

# 扫描文件 数据清理 去除scanid和n
for index in range(FlightPath.shape[0]-1):
        print(index)
        LIDARPoints.drop([(index+1)*533],inplace=True)

# 初始化飞行坐标数组
x = np.zeros(34)
y = np.zeros(34)

# 读取飞行 x和y的坐标数组
for index in range(FlightPath.shape[0]):
    x[index] = FlightPath.values[index][0]
    y[index] = FlightPath.values[index][1]
# 单独绘制飞行路径
plt.plot(x, y, 'r-o', color="red")
# 创建新的绘图窗口
plt.figure()

# 每一个循环绘制一次扫描
for index in range(FlightPath.shape[0]-1):
    # 飞行坐标绘制
    x = FlightPath.values[index][0]
    y = FlightPath.values[index][1]
    plt.plot(x, y, 'r-o',color="red")
    # 扫描绘制
    for index1 in range(533):
        # alph是倾斜角 distance是距离长度
        alph = LIDARPoints.values[index*533+index1][0]
        distance = LIDARPoints.values[index*533+index1][1]
        # 扫描点的坐标根据
        # scanX = x + math.cos(alph) * distance
        # scanY = y + math.sin(alph) * distance
        plt.plot(x + math.cos(alph) * distance,
                 y + math.sin(alph) * distance,
                 'r-o', color="green")
    # 创建新的绘图窗口
    plt.figure()

plt.show()








