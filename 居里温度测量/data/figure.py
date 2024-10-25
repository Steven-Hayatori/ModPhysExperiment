import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

# 设置字体为 SimHei（黑体），以支持中文显示
rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 读取 Excel 表格
data = pd.read_excel('data.xlsx')

# 确保数据中有 T 温度和 M 振幅这两列
T = data['T']  # 温度
M = data['M']  # 振幅

# --- 创建第一个图形：T 对 M 的折线图 ---
plt.figure(figsize=(10, 6))
plt.plot(T, M, marker='o', color='b', linestyle='-', label='振幅 vs 温度')

# 添加标题和坐标轴标签
plt.title('振幅与温度关系图')
plt.xlabel('温度 (摄氏度)')
plt.ylabel('振幅 (V)')

# 去除图例和网格
plt.grid(False)
plt.legend().remove()

# 展示第一个图形
plt.show()

# --- 计算斜率 ---
# 计算每个相邻点的斜率
slopes = np.diff(M) / np.diff(T)

# 舍弃最后一个温度点，保证 X 和 Y 维度一致
T_trimmed = T[:-1]  # 去掉最后一个点，维度与 slopes 匹配

# --- 创建第二个图形：斜率随温度变化 ---
plt.figure(figsize=(10, 6))
plt.plot(T_trimmed, slopes, marker='x', color='r', linestyle='--', label='斜率 vs 温度')

# 添加标题和坐标轴标签
plt.title('斜率与温度关系图')
plt.xlabel('温度 (摄氏度)')
plt.ylabel('斜率')

# 显示图例和网格
plt.legend()
plt.grid(True)

# 展示第二个图形
plt.show()
